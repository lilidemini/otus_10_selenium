from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    PRODUCTS_PAGE_URL = ['iphone', 'imac', 'component/monitor/samsung-syncmaster-941bw', 'camera/canon-eos-5d']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".list-unstyled h2")
    BTN_ADDED_CART = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".thumbnails")
    PRODUCT_NAV = (By.CSS_SELECTOR, 'ul.nav.nav-tabs')
