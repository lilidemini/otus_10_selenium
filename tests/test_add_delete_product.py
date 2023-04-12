from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_main_page import AdminMainPage
from page_objects.products_page import ProductsPage
from test_data.users import AdminCredentials

NEW_PRODUCT = "iPod Touch"


def test_add_new_product(browser, url):
    AdminLoginPage(browser).open_admin_login_page(url)
    AdminLoginPage(browser).login_as_admin(AdminCredentials.ADMIN_USERNAME, AdminCredentials.ADMIN_PASSWORD)
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser) \
        .click_add_new_product_button() \
        .fill_all_required_fields(NEW_PRODUCT) \
        .click_save_new_product_button() \
        .check_product_modified_alert_text() \
        .filter_products_list_by_product_name(NEW_PRODUCT) \
        .check_product_in_product_list(NEW_PRODUCT)


def test_delete_product(browser, url):
    AdminLoginPage(browser).open_admin_login_page(url)
    AdminLoginPage(browser).login_as_admin(AdminCredentials.ADMIN_USERNAME, AdminCredentials.ADMIN_PASSWORD)
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser) \
        .filter_products_list_by_product_name(NEW_PRODUCT) \
        .delete_selected_products() \
        .check_deleted_product_in_product_list(NEW_PRODUCT)
