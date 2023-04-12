from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[title='Add New']")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    META_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    NAV_TABS = (By.CSS_SELECTOR, ".nav-tabs")
    NAV_TAB_DATA = (By.CSS_SELECTOR, ".nav-tabs > li:nth-child(2)")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    NAV_TAB_SEO = (By.CSS_SELECTOR, ".nav-tabs > li:nth-child(11)")
    KEYWORD_INPUT = (By.CSS_SELECTOR, "[placeholder = 'Keyword']")
    SAVE_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PRODUCT_MODIFIED_ALERT = (By.CSS_SELECTOR, ".alert-dismissible")
    PRODUCT_MODIFIED_ALERT_TEXT = "Success: You have modified products!"
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, "input#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "button#button-filter")
    FILTERED_PRODUCT_LIST = (By.CSS_SELECTOR, "tbody > tr > td.text-start")
    BACK_BUTTON = (By.CSS_SELECTOR, "a[title='Back']")
    SELECT_ALL_CHECKBOXES = (By.CSS_SELECTOR, "input[type=checkbox]")
    DELETE_BUTTON = (By.CSS_SELECTOR, "[title='Delete']")
    EMPTY_RESULTS = (By.CSS_SELECTOR, "tbody > tr > td")

    def click_add_new_product_button(self):
        self.click_element(self.element(self.ADD_NEW_PRODUCT_BUTTON))
        return self

    def click_save_new_product_button(self):
        self.click_element(self.element(self.SAVE_NEW_PRODUCT_BUTTON))
        return self

    def fill_required_fields_on_tab_general(self, new_product_name):
        self.input_value(self.element(self.PRODUCT_NAME_INPUT), new_product_name)
        self.input_value(self.element(self.META_TITLE_INPUT), new_product_name)
        return self

    def fill_required_fields_on_tab_data(self, new_product_name):
        self.click_element(self.element(self.NAV_TAB_DATA))
        self.input_value(self.element(self.MODEL_INPUT), new_product_name)
        return self

    def fill_required_fields_on_tab_seo(self, new_product_name):
        self.click_element(self.element(self.NAV_TAB_SEO))
        self.input_value(self.element(self.KEYWORD_INPUT), new_product_name)
        return self

    def fill_all_required_fields(self, new_product_name):
        self.fill_required_fields_on_tab_general(new_product_name)
        self.fill_required_fields_on_tab_data(new_product_name)
        self.fill_required_fields_on_tab_seo(new_product_name)
        return self

    def check_product_modified_alert_text(self):
        assert self.element(self.PRODUCT_MODIFIED_ALERT).text == self.PRODUCT_MODIFIED_ALERT_TEXT, \
            "Unexpected alert, expected success alert"
        return self

    def return_to_products_page(self):
        self.click_element(self.element(self.BACK_BUTTON))
        return self

    def filter_products_list_by_product_name(self, product_name):
        self.input_value(self.element(self.FILTER_PRODUCT_NAME), product_name)
        self.click_element(self.element(self.FILTER_BUTTON))
        return self

    def check_product_in_product_list(self, product_name):
        for i in self.elements(self.FILTERED_PRODUCT_LIST):
            assert product_name in i.text, "Searching product is not in filtered list of products"

    def select_all_checkboxes(self):
        self.click_element(self.element(self.SELECT_ALL_CHECKBOXES))
        return self

    def click_delete_button(self):
        self.click_element(self.element(self.DELETE_BUTTON))
        return self

    def confirm_deletion(self):
        alert = WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert.accept()
        return self

    def delete_selected_products(self):
        self.select_all_checkboxes()
        self.click_delete_button()
        self.confirm_deletion()
        return self

    def check_deleted_product_in_product_list(self, product_name):
        for i in self.elements(self.EMPTY_RESULTS):
            assert i.text == "No results!", "Products was not deleted"
