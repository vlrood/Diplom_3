from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import scripts


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def set_text_on_filed(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def wait_loading_page(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    def wait_loading_change_url(self, url):
        WebDriverWait(self.driver, 15).until(expected_conditions.url_contains(url))

    def drag_and_drop(self, locator_1, locator_2):
        source = WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(locator_1))
        target = WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(locator_2))
        self.driver.execute_script(scripts.script_drag_and_drop, source, target)
