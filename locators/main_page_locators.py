from selenium.webdriver.common.by import By


class MainLocators:
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')
    INGREDIENT = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    CLOSE_WINDOW = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    POP_UP_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox__sCy8X")]')
    COUNTER = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]/div[1]/p')
    BASKET = (By.XPATH, '//span[text()="Перетяните булочку сюда (низ)"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    TEXT_ORDER = (By.XPATH, '//p[@class="undefined text text_type_main-small mb-2"]')
