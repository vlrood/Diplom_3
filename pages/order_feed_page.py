import allure
from data import Urls
from locators.order_feed_page_locators import OrderLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Ожидаем загрузку страницы ленты заказов')
    def wait_loading_order_page(self):
        self.wait_loading_change_url(Urls.ORDER_FEED)

    @allure.step('Ожидаем появления новых данных на странице')
    def wait_updating_data_on_page(self):
        self.wait_loading_page(OrderLocators.ORDER)

    @allure.step('Ожидаем новый номер в разаделе "В работе')
    def wait_new_number_in_prepared(self):
        self.wait_loading_page(OrderLocators.NUMBER_PREPARED)

    @allure.step('Нажимем на заказ')
    def click_on_order(self):
        element = self.wait_and_find_element(OrderLocators.ORDER)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Отслеживаем отображение всплывающего окна')
    def pop_window_is_displayed(self):
        pop_up_window = self.wait_and_find_element(OrderLocators.ORDER_POP_UP_WINDOW)
        return pop_up_window.is_displayed()

    @allure.step('Получаем номер заказа в Истории заказов')
    def get_number_order_of_history(self):
        number = self.wait_and_find_element(OrderLocators.NUMBER_ORDER_ON_HISTORY)
        return number.text

    @allure.step('Получаем номер заказа в ленте заказов')
    def get_number_order_of_feed(self):
        number = self.wait_and_find_element(OrderLocators.NUMBER_ORDERS_ON_FEED)
        return number.text

    @allure.step('Получаем номер счетчика')
    def get_number_of_counter(self, locator):
        counter = self.wait_and_find_element(locator)
        return counter.text

    @allure.step('Получаем номер заказа в разделе "В работе"')
    def get_number_of_prepared(self):
        number = self.wait_and_find_element(OrderLocators.NUMBER_PREPARED)
        return number.text
