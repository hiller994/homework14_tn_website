import allure
from selene import browser, be, have


class PromoPage:

    @allure.step('Открываем браузер')
    def open(self):
        browser.open('/promotions')

    @allure.step('Отображение главной акции')
    def header_promo(self):
        browser.element('[class="promotions-header"]').should(be.visible)

    @allure.step('Отображение остальных акций')
    def other_promo(self):
        browser.element('[class="promotions-list"]').should(be.visible)

    @allure.step('Переход по акции')
    def click_header_promo(self):
        browser.element('[class="promotions-header"]').click()
        browser.element('[class="promotions-item__content"]').should(be.visible)