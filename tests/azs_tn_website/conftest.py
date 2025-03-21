import pytest
from selene import browser, be, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    #browser.config.window_height = 1080  # высота браузера
    #browser.config.window_width = 1920  # ширина браузера
    #browser.open('https://duckduckgo.com/')
    browser.config.base_url = 'https://azs.tatneft.ru'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)
    browser.quit()