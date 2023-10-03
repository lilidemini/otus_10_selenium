from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    PRODUCTS_PAGE_URL = ['en-gb/product/desktops/mac/imac', 'en-gb/product/iphone']
    BREADCRUMB_ITEM = (By.CSS_SELECTOR, ".breadcrumb li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".list-unstyled h2")
    BTN_ADDED_CART = (By.CSS_SELECTOR,  'button#button-cart')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".magnific-popup .img-thumbnail")
    PRODUCT_NAV = (By.CSS_SELECTOR, '.nav-tabs')


