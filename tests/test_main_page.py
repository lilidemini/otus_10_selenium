from page_objects.main_page import MainPage
import pytest


def test_elements_on_catalog_page(url, browser):
    MainPage(browser) \
        .open_main_page(url) \
        .check_elements_on_page()


@pytest.mark.parametrize("currency, current_currency",
                         [(MainPage.CURRENCY_EURO, "€"), (MainPage.CURRENCY_GBR, "£"), (MainPage.CURRENCY_USD, "$")])
def test_change_currency(url, browser, currency, current_currency):
    MainPage(browser) \
        .open_main_page(url) \
        .change_currency(currency) \
        .check_current_currency(current_currency)
