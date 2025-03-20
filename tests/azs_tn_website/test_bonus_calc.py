import allure
from allure_commons.types import Severity

from tests.models.pages.bonus_page import BonusCalc
import conftest

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Andrey Ignatov")
@allure.feature("Сайт АЗС ТН")
@allure.story("Тест подсчета бонусов. PROD")
@allure.link("https://azs.tatneft.ru/loyal", name="Testing")

def test_bonus_calc(setup_browser):
    loyal_page = BonusCalc()
    loyal_page.open()

    loyal_page.click_slider(50000)
    loyal_page.should_bonus("2 500")