from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductCardPage(BasePage):
    PRODUCT_URLS = ['iphone', 'imac', 'component/monitor/samsung-syncmaster-941bw', 'camera/canon-eos-5d']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".list-unstyled h2")
    BTN_ADDED_CART = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".thumbnails")
    PRODUCT_NAV = (By.CSS_SELECTOR, 'ul.nav.nav-tabs')

    def open_product_card_page(self, url, product_url):
        self.browser.get(url + '/en-gb/product/' + product_url)
        return self

    def check_elements_on_page(self):
        self.element(self.BREADCRUMB_ITEMS)
        self.element(self.PRODUCT_NAME)
        self.element(self.PRODUCT_PRICE)
        self.element(self.BTN_ADDED_CART)
        self.element(self.PRODUCT_NAV)
