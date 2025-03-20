import allure
from selene import browser, have, be


class MainPage:
    @allure.step("Открываем браузер")
    def open(self):
        browser.open('/')

    @allure.step("Проверка основных элементов на странице")
    def should_element(self):
        browser.element('[class="highlight-title"]').should(have.text('Будь в курсе самых выгодных акций и предложений!'))
        browser.element('[class="left-block__background"]').should(be.visible)
        browser.element('[class="right-block"]').should(be.visible)
        browser.element('[id="background-video"]').should(be.visible)