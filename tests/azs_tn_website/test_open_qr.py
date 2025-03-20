import allure
from selene import browser, have, be
from tests.models.pages.qr_page import QrPage
from allure_commons.types import Severity

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Andrey Ignatov")
@allure.feature("Сайт АЗС ТН")
@allure.story("Тест отображения QR-кода для скачивания мп. PROD")
@allure.link("https://azs.tatneft.ru/loyal", name="Testing")

def test_open_qr(setup_browser):
    qr_page = QrPage()
    qr_page.open()
    qr_page.open_qr()
    qr_page.visible_qr()