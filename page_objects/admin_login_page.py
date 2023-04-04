from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class AdminLoginPage(BasePage):
    ADMIN_LOGIN_URL = "/admin"
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, 'OpenCart')

    def open_page(self, base_url):
        self.browser.get(base_url)



