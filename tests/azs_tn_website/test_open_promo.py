from selene import browser, be
from tests.models.pages.promo_page import PromoPage

def test_open_sale(setup_browser):
    promo_page = PromoPage()
    promo_page.open()
    promo_page.header_promo()
    promo_page.other_promo()
    promo_page.click_header_promo()