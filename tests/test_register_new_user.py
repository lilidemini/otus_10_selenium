from page_objects.register_page import RegisterPage
from test_data.users import NewUser


def test_elements_on_register_page(url, browser):
    RegisterPage(browser) \
        .open_register_page(url) \
        .check_elements_on_page()


def test_register_new_user(url, browser):
    RegisterPage(browser) \
        .open_register_page(url) \
        .fill_reqiured_fields(NewUser.NEW_USER_FIRST_NAME, NewUser.NEW_USER_LAST_NAME,
                              NewUser.NEW_USER_EMAIL, NewUser.NEW_USER_PASSWORD) \
        .agree_privacy_policy_checkbox()\
        .click_continue()\
        .check_success_registration_message()
