import allure
from data import Urls
from locators.personal_account_page_locators import AccountLocators
from pages.base_page import BasePage


class PersonalPage(BasePage):
    @allure.step('Нажимем на личный кабинет')
    def click_on_personal_account(self):
        element = self.wait_and_find_element(AccountLocators.PERSONAL_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидаем загрузку личного кабинета')
    def wait_loading_personal_page(self):
        self.wait_loading_change_url(Urls.PROFILE_URL)

    @allure.step('Нажимем на история заказов')
    def click_on_orders_history(self):
        element = self.wait_and_find_element(AccountLocators.ORDERS_HISTORY)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Нажимем на кнопку "Выход"')
    def click_on_button_exit(self):
        self.click_on_element(AccountLocators.BUTTON_EXIT)

    @allure.step('Авторизуемся')
    def account(self, email, password):
        self.set_text_on_filed(AccountLocators.LOGIN_EMAIL_INPUT, email)
        self.set_text_on_filed(AccountLocators.LOGIN_PASSWORD_INPUT, password)
        self.click_on_element(AccountLocators.LOGIN_SUBMIT)

    @allure.step('Ожидаем прогрузку страницы, чтобы совершить нажатие')
    def wait_for_loading_to_click(self):
        self.wait_loading_page(AccountLocators.SECTION_SAUCES)

    @allure.step('Ожидаем прогрузку страницы авторизации')
    def wait_login_page(self):
        self.wait_loading_change_url(Urls.LOGIN_URL)

    @allure.step('Переход в личный кабинет')
    def go_to_the_personal_account(self):
        self.wait_for_loading_to_click()
        self.click_on_personal_account()
        self.wait_loading_personal_page()

    @allure.step('Выход из личного кабинета')
    def logout_to_personal_account(self):
        self.click_on_button_exit()
        self.wait_login_page()

