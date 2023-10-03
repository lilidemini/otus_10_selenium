from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By

class CatalogPage(BasePage):
    CATALOGS_PAGE_URL = ['en-gb/catalog/desktops', 'en-gb/catalog/laptop-notebook']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    CATALOG_NAME = (By.CSS_SELECTOR, "h2")
    SIDEBAR = (By.CSS_SELECTOR, "#column-left")
    SORT= (By.CSS_SELECTOR, "#input-sort")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CATALOG_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")