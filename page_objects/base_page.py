from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def element_is_present(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def input(self, locator, value):
        find_field = self.wait.until(EC.presence_of_element_located(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)
