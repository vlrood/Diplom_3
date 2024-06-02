import allure
from data import Urls, DataText
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Нажимаем на "Конструктор", проверяем ссылку')
    def test_click_on_constructor_driver_transition_completed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.wait_page()
        main_page.click_on_order_feed()
        main_page.click_on_constructor()

        assert driver.current_url == Urls.BASE_URL

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Нажимаем на "Лента заказов", проверяем ссылку')
    def test_click_on_order_feed_driver_transition_completed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.wait_page()
        main_page.click_on_order_feed()

        assert Urls.ORDER_FEED in driver.current_url

    @allure.title('Проверка, что при нажатии ингредиента всплывет окно')
    @allure.description('Нажимаем на ингредиент, проверяем отображение всплывающего окна')
    def test_click_on_ingredient_driver_windows_pop_up(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.wait_page()
        main_page.click_on_ingredient()

        assert main_page.check_pop_up_window(), 'Pop-window does not exist'

    @allure.title('Проверка, что, при нажатии на крестик, всплывающее окно закрывается')
    @allure.description('Нажимем на крестик, проверяем, что окно не отображается')
    def test_close_pop_up_window_driver_closed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.wait_page()
        main_page.click_on_ingredient()
        main_page.click_on_close_window()

        assert main_page.wait_invisibility_pop_up_window() is True

    @allure.title('Проверка, что счетчик увеличивается при добавлении ингридиента в корзину')
    @allure.description('Добавляем ингридиент в корзину, сравниваем счетчик до и после добавления')
    def test_increasing_ingredient_counter_driver_create_order_increased(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        before = main_page.get_number_counter()
        main_page.add_ingredient_to_basket()
        main_page.wait_page()
        after = main_page.get_number_counter()

        assert before != after

    @allure.title('Проверка возможности авторизованного пользователя оформить заказ')
    @allure.description('Нажимем на кнопку "Оформить заказ", проверяем текст на всплывшем окне')
    def test_authorized_user_can_place_an_order_driver_login(self, login, driver):
        main_page = MainPage(driver)
        main_page.wait_page()
        main_page.click_on_checkout()

        assert main_page.get_text_to_order_pop_up_window() == DataText.ORDER_PREPARED
