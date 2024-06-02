import allure
from data import Urls
from pages.personal_account_page import PersonalPage


class TestPersonalAccount:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('Нажимаем на "Личный кабиент", проверяем ссылку')
    def test_transition_to_personal_account_driver_login_transferred(self, driver, login):
        personal_page = PersonalPage(driver)
        personal_page.wait_for_loading_to_click()
        personal_page.click_on_personal_account()
        personal_page.wait_loading_personal_page()

        assert Urls.PROFILE_URL == driver.current_url

    @allure.title('Проверка перехода по клику на "История заказов" в личном кабинете')
    @allure.description('Переходим в личный кабинет, нажимаем "История заказов", проверяем ссылку')
    def test_transition_to_history_orders_login_transferred(self, driver, login):
        personal_page = PersonalPage(driver)
        personal_page.go_to_the_personal_account()
        personal_page.click_on_orders_history()

        assert Urls.ORDER_HISTORY in driver.current_url

    @allure.title('Проверка выхода из личного кабинет')
    @allure.description('Выходим из личного кабинета по кнопке "Выход", проверяем ссылку')
    def test_logout_from_account_driver_login_logout_success(self, driver, login):
        personal_page = PersonalPage(driver)
        personal_page.go_to_the_personal_account()
        personal_page.logout_to_personal_account()

        assert Urls.LOGIN_URL == driver.current_url
