import allure
from selene import browser, have, be


class QrPage:
    @allure.step("Открываем браузер")
    def open(self):
        browser.open('/loyal')

    @allure.step("Открываем форму с QR-кодом для загрузки мп")
    def open_qr(self):
        browser.element('[class="btn-app desktop"]').click()
        browser.element('[class="mobile-app-popup"]').should(have.text('Скачайте приложение'))

    @allure.step("Проверка видимости QR")
    def visible_qr(self):
        browser.element('[src="/_nuxt/img/qr-code.471c5bc.png"]').should(be.visible)
