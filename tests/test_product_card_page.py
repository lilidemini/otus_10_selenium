import pytest

from page_objects.product_card_page import ProductCardPage


@pytest.mark.parametrize("product_url", ProductCardPage.PRODUCT_URLS)
def test_elements_on_catalog_page(url, browser, product_url):
    ProductCardPage(browser) \
        .open_product_card_page(url, product_url) \
        .check_elements_on_page()
