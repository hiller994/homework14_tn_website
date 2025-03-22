import allure
from allure_commons.types import Severity
from tests.models.pages.promo_page import PromoPage

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Andrey Ignatov")
@allure.feature("Сайт АЗС ТН")
@allure.story("Тест страницы промо. PROD")
@allure.link("https://azs.tatneft.ru/promotions", name="Testing")

def test_open_sale(setup_browser):
    promo_page = PromoPage()
    promo_page.open()
    promo_page.header_promo()
    promo_page.other_promo()
    promo_page.click_header_promo()