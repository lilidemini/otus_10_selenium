from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    LOGIN_PAGE_LINK = (By.LINK_TEXT, "login page")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    DEFAULT_SUBSCRIBE = (By.CSS_SELECTOR, 'input[value="0"]')
