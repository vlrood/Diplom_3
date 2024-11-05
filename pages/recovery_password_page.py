import allure
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls, DataRecovery
from locators.recovery_password_page_locators import PasswordLocators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):
    @allure.step('Ожидаем загрузку страницы авторизации')
    def wait_loading_login_page(self):
        self.wait_loading_change_url(Urls.LOGIN_URL)

    @allure.step('Ожидаем загрузку форму восстановления пароля')
    def wait_loading_reset_password_page(self):
        self.wait_loading_change_url(Urls.RESET_PASSWORD)

    @allure.step('Прокручиваем до "Восстановление пароля"')
    def scroll_to_the_element(self):
        element = self.wait_and_find_element(PasswordLocators.RECOVERY_PASSWORD_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5)

    @allure.step('Нажимаем на "Восстановленить пароль"')
    def click_on_recovery_password(self):
        element = self.wait_and_find_element(PasswordLocators.RECOVERY_PASSWORD_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Вводим почту для восстановления пароля')
    def set_email(self):
        self.set_text_on_filed(PasswordLocators.EMAIL_INPUT, DataRecovery.EMAIL)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.click_on_element(PasswordLocators.RECOVERY_BUTTON)

    @allure.step('Заполняем поле "Пароль"')
    def set_recovery_password(self):
        self.set_text_on_filed(PasswordLocators.PASSWORD_INPUT, DataRecovery.PASSWORD)

    @allure.step('Нажимаем на скрыть/показать пароль')
    def click_on_display_button(self):
        element = self.wait_and_find_element(PasswordLocators.DISPLAY_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получаем класс поля "Пароль"')
    def get_class_name_password_filed(self):
        new_password = self.wait_and_find_element(PasswordLocators.NEW_PASSWORD_FILED)
        return new_password.get_attribute('class')

    @allure.step('Переходим на форму восстановления пароля')
    def transit_to_recovery_password_page(self):
        self.wait_loading_login_page()
        self.scroll_to_the_element()
        self.click_on_recovery_password()

    @allure.step('Переходим на форму подтверждения восстановления пароля')
    def recovery_password(self):
        self.set_email()
        self.click_on_recovery_button()
        self.wait_loading_reset_password_page()
