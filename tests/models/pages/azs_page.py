import allure
from selene import browser, have

class AzsPage:
    @allure.step('Открываем браузер')
    def open(self):
        browser.open('/locator')

    @allure.step('Вводим адрес АЗС')
    def type_azs(self, value_address):
        browser.element('[placeholder="Поиск АЗС"]').type(value_address)

    @allure.step('Проверяем результат')
    def azs_results(self, value_results):
        browser.element('[class="gas-station gas-station--filtered"]').should(have.text(value_results))