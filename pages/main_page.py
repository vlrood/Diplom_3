import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Ожидаем загрузку главной страницы')
    def wait_page(self):
        self.wait_loading_page(MainLocators.INGREDIENT)

    @allure.step('Нажимаем на конструктор')
    def click_on_constructor(self):
        element = self.wait_and_find_element(MainLocators.CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Нажимаем на "Лента заказов"')
    def click_on_order_feed(self):
        element = self.wait_and_find_element(MainLocators.ORDER_FEED)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Нажимаем на ингридиент')
    def click_on_ingredient(self):
        element = self.wait_and_find_element(MainLocators.INGREDIENT)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверяем отображение всплывшего окна')
    def check_pop_up_window(self):
        pop_up_window = self.wait_and_find_element(MainLocators.POP_UP_WINDOW)
        return pop_up_window.is_displayed()

    @allure.step('Нажимаем на крестик всплывающего окна')
    def click_on_close_window(self):
        close_window = self.wait_and_find_element(MainLocators.CLOSE_WINDOW)
        close_window.click()

    @allure.step('Проверяем отсутствие всплывшего окна')
    def wait_invisibility_pop_up_window(self):
        if WebDriverWait(self.driver, 5).until(
                expected_conditions.invisibility_of_element(MainLocators.POP_UP_WINDOW)):
            return True

    @allure.step('Получаем текст счетчика количества ингридиентов')
    def get_text_counter(self):
        counter = self.wait_and_find_element(MainLocators.COUNTER)
        return counter.text

    @allure.step('Добавляем ингридиент в заказ')
    def add_ingredient_to_basket(self):
        self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.BASKET)

    @allure.step('Получаем номер счетчика ингридиента')
    def get_number_counter(self):
        number = self.wait_and_find_element(MainLocators.COUNTER)
        return number.text

    @allure.step('Нажимем на кнопку "Оформить заказ"')
    def click_on_checkout(self):
        element = self.wait_and_find_element(MainLocators.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получаем тескт, отображенном во всплывшем окне')
    def get_text_to_order_pop_up_window(self):
        title_popup_window = self.wait_and_find_element(MainLocators.TEXT_ORDER)
        return title_popup_window.text
