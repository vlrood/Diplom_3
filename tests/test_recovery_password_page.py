import allure
from data import Urls
from pages.recovery_password_page import RecoveryPasswordPage


class TestRecoveryPassword:
    @allure.title('Проверка перехода по "Восстановнить пароль" на форму восстановления пароля')
    @allure.description('Нажимаем на "Восстановить пароль", проверяем ссылку')
    def test_click_on_recovery_button_driver_transition_completed(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.LOGIN_URL)
        recovery_page.transit_to_recovery_password_page()

        assert Urls.RECOVERY_PASSWORD in driver.current_url

    @allure.title('Проверка пеерехода при нажатии на кнопку "Восстановить"')
    @allure.description('Ввод почты, нажатие кнопки "Восстановить", проверка ссылки')
    def test_click_on_button_recovery_driver_transition_completed(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.LOGIN_URL)
        recovery_page.transit_to_recovery_password_page()
        recovery_page.recovery_password()

        assert Urls.RESET_PASSWORD in driver.current_url

    @allure.title('Проверка посвечивания и отображения пароля при клику на показать/скрыть')
    @allure.description('Нажимаем на скрыть/показать, проверяем изменение класса элемента')
    def test_click_on_display_button_driver_filed_is_display(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.LOGIN_URL)
        recovery_page.transit_to_recovery_password_page()
        recovery_page.recovery_password()
        non_active = recovery_page.get_class_name_password_filed()
        recovery_page.set_recovery_password()
        recovery_page.click_on_display_button()
        active = recovery_page.get_class_name_password_filed()

        assert non_active != active
