import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import have

from tests.models.pages.azs_page import AzsPage

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Andrey Ignatov")
@allure.feature("Сайт АЗС ТН")
@allure.story("Тест поиска АЗС. PROD")
@allure.link("https://azs.tatneft.ru/loyal", name="Testing")

def test_search_azs(setup_browser):
    azs_page = AzsPage()
    azs_page.open()
    azs_page.type_azs('г.Казань, ул.Гаврилова, 6 А')
    azs_page.azs_results('АЗС 200')