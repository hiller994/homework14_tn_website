import pytest
from selene import browser, be, have

from utils import attach


@pytest.fixture(scope='session')
def setup_browser():
    browser.config.window_height = 1080  # высота браузера
    browser.config.window_width = 1920  # ширина браузера
    #browser.open('https://duckduckgo.com/')
    browser.config.base_url = 'https://azs.tatneft.ru'
    yield
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)
    browser.quit()