import allure
from selene import browser, be, have
from allure_commons.types import Severity

from tests.models.pages.main_page import MainPage

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Andrey Ignatov")
@allure.feature("Сайт АЗС ТН")
@allure.story("Тест главной страницы. PROD")
@allure.link("https://azs.tatneft.ru/", name="Testing")

def test_open_main_page(setup_browser):
    main_page = MainPage()
    main_page.open()
    main_page.should_element()