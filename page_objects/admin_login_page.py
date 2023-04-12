from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, 'OpenCart')

    def open_admin_login_page(self, url):
        self.browser.get(url + '/administration/')
        return self

    def check_elements_on_page(self):
        self.element(self.USERNAME_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.LOGIN_BUTTON)
        self.element(self.FORGOTTEN_PASSWORD)
        self.element(self.OPENCART_LINK)
        return self

    def login_as_admin(self, username, password):
        self.input_value(self.element(self.USERNAME_INPUT), username)
        self.input_value(self.element(self.PASSWORD_INPUT), password)
        self.click_element(self.element(self.LOGIN_BUTTON))
        return self
