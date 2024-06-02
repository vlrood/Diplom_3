import allure
import pytest
import helper
from data import Urls
from locators.order_feed_page_locators import OrderLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalPage


class TestOrderFeedPage:
    @allure.title('Проверка, что при нажатии на заказ всплывет окно заказа')
    @allure.description('Нажимаем на заказ, проверяем отображение окна')
    def test_click_on_order_driver_pop_up_window_opened(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.open_page(f'{Urls.BASE_URL}{Urls.ORDER_FEED}')
        order_page.wait_loading_order_page()
        order_page.click_on_order()

        assert order_page.pop_window_is_displayed(), 'Pop-up window does not exist'

    @allure.title('Проверка отображения заказа пользователя в ленте заказов')
    @allure.description('Сравниваем номер заказа в истории заказов и в ленте заказов')
    def test_order_displayed_in_order_feed_driver_create_and_delete_user_login_visible(self, create_and_delete_user,
                                                                                       driver, login):
        profile_page = PersonalPage(driver)
        order_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        profile_page.go_to_the_personal_account()
        profile_page.click_on_orders_history()
        helper.create_order(create_and_delete_user)
        history = order_page.get_number_order_of_history()
        main_page.click_on_order_feed()
        number = order_page.get_number_order_of_feed()

        assert history in number

    @allure.title('Проверка увеличения счетчиков при новом заказе')
    @allure.description('Проверяем номер счетчика в истории заказа среди остальных заказов')
    @pytest.mark.parametrize('counter', [OrderLocators.ALL_THE_TIME_COUNTER, OrderLocators.TODAY_COUNTER])
    def test_counter_increase_driver_create_and_delete_user_login_counter_increased(self, driver, login, counter,
                                                                                    create_and_delete_user):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        profile_page = PersonalPage(driver)
        profile_page.go_to_the_personal_account()
        main_page.click_on_order_feed()
        before_order = order_page.get_number_of_counter(counter)
        main_page.click_on_constructor()
        helper.create_order(create_and_delete_user)
        main_page.click_on_order_feed()
        after_order = order_page.get_number_of_counter(counter)

        assert before_order != after_order

    @allure.title('Проверка отображения заказа в разделе "В работе"')
    @allure.description('Совершаем заказ, проверяем раздел "В работе"')
    def test_number_order_appears_in_prepared_driver_create_and_delete_user_login_appeared(self, driver, login,
                                                                                           create_and_delete_user):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        profile_page = PersonalPage(driver)
        profile_page.go_to_the_personal_account()
        helper.create_order(create_and_delete_user)
        profile_page.click_on_orders_history()
        history = order_page.get_number_order_of_history()
        main_page.click_on_order_feed()
        order_page.wait_updating_data_on_page()
        prepared = order_page.get_number_of_prepared()

        assert history == '#' + prepared
