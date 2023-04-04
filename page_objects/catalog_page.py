from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CatalogPage(BasePage):
    CATALOGS_PAGE_URL = ['desktops', 'laptop-notebook', 'tablet', 'smartphone', 'camera', 'mp3-players']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    CATALOG_NAME = (By.CSS_SELECTOR, "h2")
    SIDEBAR = (By.CSS_SELECTOR, "#column-left")
    SORT= (By.CSS_SELECTOR, "#input-sort")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CATALOG_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
