from page_objects.catalog_page import CatalogPage
import pytest


@pytest.mark.parametrize("catalog_url", CatalogPage.CATALOG_URLS)
def test_elements_on_catalog_page(url, browser, catalog_url):
    CatalogPage(browser) \
        .open_catalog_page(url, catalog_url) \
        .check_elements_on_page()
