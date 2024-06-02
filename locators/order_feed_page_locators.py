from selenium.webdriver.common.by import By


class OrderLocators:
    ORDER = (By.XPATH, '//ul/li[1]/a[@class="OrderHistory_link__1iNby"]')
    ORDER_POP_UP_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_orderBox__1xWdi")]')
    NUMBER_ORDER_ON_HISTORY = (By.XPATH, '//li[1]//div[1]/p[@class="text text_type_digits-default"]')
    NUMBER_ORDERS_ON_FEED = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    ALL_THE_TIME_COUNTER = (By.XPATH, '//div[2]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    TODAY_COUNTER = (By.XPATH, '//div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    NUMBER_PREPARED = (By.XPATH, '//ul[2]/li[@class="text text_type_digits-default mb-2"]')

