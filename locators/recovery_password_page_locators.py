from selenium.webdriver.common.by import By


class PasswordLocators:
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/forgot-password"]')
    EMAIL_INPUT = (By.XPATH, '//input[contains(@class, "text input__textfield text")]')
    RECOVERY_BUTTON = (By.XPATH, '//button[contains(@class, "button_button__33qZ0 ")]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    DISPLAY_BUTTON = (By.XPATH, '//div[contains(@class, "input__icon-action")]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Введите новый пароль"]')
    NEW_PASSWORD_FILED = (By.XPATH, '//label[text()="Пароль"]')
