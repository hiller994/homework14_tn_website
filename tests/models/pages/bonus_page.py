import allure
from selene import browser, have
from selenium.webdriver.common.action_chains import ActionChains

class BonusCalc:
    @allure.step("Открываем браузер")
    def open(self):
        browser.open('/loyal')
        #browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        #browser.driver.execute_script("$('#fixedban').remove()")
        #browser.driver.execute_script("$('footer').remove()")

    @allure.step("Выставляем слайдер трат")
    def click_slider(self, cost):
        # Находим элемент ползунка
        slider = browser.element('input[type="range"]')
        # Получаем размеры ползунка
        slider_rect = slider.locate().rect
        slider_width = slider_rect['width']
        # Вычисляем смещение для нужного значения (например, 25000)
        min_value = 1000
        max_value = 50000
        target_value = cost
        offset_x = (target_value - min_value) / (max_value - min_value) * slider_width
        # Перемещаем ползунок с помощью Actions
        actions = ActionChains(browser.driver)
        actions.click_and_hold(slider.locate()).move_by_offset(offset_x, 0).release().perform()

    @allure.step("Проверяем подсчет бонусов")
    def should_bonus(self, val_bonus):
        browser.element('[class="calc__total"]').should(have.text(f'= {val_bonus} бонусов'))