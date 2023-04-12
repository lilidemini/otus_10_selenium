from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 2).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def click_element(self, element):
        ActionChains(self.browser).move_to_element(element).pause(0.3).click().perform()

    def input_value(self, element, value):
        self.click_element(element)
        element.clear()
        element.send_keys(value)
        return self

    def scroll_to_element(self, element):
        ActionChains(self.browser).scroll_to_element(element).perform()

    def get_element_text(self, locator):
        el = self.element(locator)
        return el.text
