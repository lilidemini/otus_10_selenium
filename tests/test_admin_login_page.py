from page_objects.admin_login_page import AdminLoginPage


def test_elements_on_login_page(url, browser):
    AdminLoginPage(browser) \
        .open_admin_login_page(url) \
        .check_elements_on_page()
