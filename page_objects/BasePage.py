from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step("Открываю url")
    def open(self, base_url):
        self.logger.info("%s: Opening base url: %s" % (self.class_name, base_url))
        self.driver.get(base_url)

    def element(self, locator):
        self.logger.info("%s: Check if element %s is present" % (self.class_name, str(locator)))
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements(self, locator):
        self.logger.info("%s: Check if elements %s are present" % (self.class_name, str(locator)))
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Выполняю клик по элементу {locator}")
    def click(self, locator):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, str(locator)))
        self.wait.until(EC.element_to_be_clickable(locator)).click()
