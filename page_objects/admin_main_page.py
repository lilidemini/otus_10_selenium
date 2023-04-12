from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminMainPage(BasePage):
    MENU = (By.CSS_SELECTOR, "#menu")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS = (By.CSS_SELECTOR, "#menu-catalog > ul > li:nth-child(2)")

    def open_products_page(self):
        self.click_element(self.element(self.MENU_CATALOG))
        self.click_element(self.element(self.PRODUCTS))
