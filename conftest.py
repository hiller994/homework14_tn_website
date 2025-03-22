import os

import pytest
from selene import browser, be, have, Config, Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Options нужен для кастомного брауера
from dotenv import load_dotenv

from utils import attach


#Версия браузера
DEFAULT_BROWSER_VERSION = '128.0' #константа для дефолтной версии браузера
def pytest_addoption(parser):
    parser.addoption( #через парсер зачитываем наши опции
        '--browser_version', #выбор версии браузера
        default='100.0' #по дефолту
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function') #autouse=True нужен, чтобы не указывать руками фикстуру в тестах
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION #это защитит от того, что не заполнили параметр

#запуск браузер селеноид
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome", # browser_name вместо хрома
        "browserVersion": browser_version, #вместо "100.0"
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver=driver)) #мы создаем свой объект браузера. В классе браузера передаем конструктор Config, в конструктор Config передаем наш driver


    yield browser
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)

    browser.quit()