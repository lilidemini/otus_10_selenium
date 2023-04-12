from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    CATALOG_URLS = ['desktops', 'laptop-notebook', 'tablet', 'smartphone', 'mp3-players']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    CATALOG_NAME = (By.CSS_SELECTOR, "h2")
    SIDEBAR = (By.CSS_SELECTOR, "#column-left")
    SORT = (By.CSS_SELECTOR, "#input-sort")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CATALOG_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")

    def open_catalog_page(self, url, catalog_url):
        self.browser.get(url + '/en-gb/catalog/' + catalog_url)
        return self

    def check_elements_on_page(self):
        self.element(self.BREADCRUMB_ITEMS)
        self.element(self.CATALOG_NAME)
        self.element(self.SIDEBAR)
        self.element(self.SORT)
        self.element(self.CATALOG_PRODUCT)
        return self
