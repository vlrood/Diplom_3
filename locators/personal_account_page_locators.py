from selenium.webdriver.common.by import By


class AccountLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')
    ORDERS_HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    BUTTON_EXIT = (By.XPATH, '//button[text()="Выход"]')
    LOGIN_EMAIL_INPUT = (By.NAME, 'name')
    LOGIN_PASSWORD_INPUT = (By.NAME, 'Пароль')
    LOGIN_SUBMIT = (By.XPATH, './/button[text()="Войти"]')
    SECTION_SAUCES = (By.XPATH, './/span[text()="Соусы"]/parent::div')
