import time
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    LOGIN_PAGE_LINK = (By.LINK_TEXT, "login page")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PRIVACY_POLICY_AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUCCESS_REGISTRATION_HEADER = (By.CSS_SELECTOR, '#content > h1')

    def open_register_page(self, url):
        self.browser.get(url + '/en-gb?route=account/register')
        return self

    def check_elements_on_page(self):
        self.element(self.FIRST_NAME_INPUT)
        self.element(self.LAST_NAME_INPUT)
        self.element(self.EMAIL_INPUT)
        self.element(self.PASSWORD_INPUT)

    def fill_reqiured_fields(self, first_name, last_name, email, password):
        self.input_value(self.element(self.FIRST_NAME_INPUT), first_name)
        self.input_value(self.element(self.LAST_NAME_INPUT), last_name)
        self.input_value(self.element(self.EMAIL_INPUT), email)
        self.input_value(self.element(self.PASSWORD_INPUT), password)
        return self

    def agree_privacy_policy_checkbox(self):
        self.click_element(self.element(self.PRIVACY_POLICY_AGREE_CHECKBOX))
        return self

    def click_continue(self):
        self.click_element(self.element(self.CONTINUE_BUTTON))
        # загрузка страницы
        time.sleep(2)
        return self

    def check_success_registration_message(self):
        assert self.get_element_text(
            self.SUCCESS_REGISTRATION_HEADER) == "Your Account Has Been Created!", "New user was not created"
