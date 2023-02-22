import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.pages import MainPage, ProductPage, AdminLoginPage, RegisterPage, CatalogPage
from selenium.common.exceptions import UnexpectedAlertPresentException


@pytest.mark.main
def test_main_page_elements(base_url, browser):
    browser.get(base_url)
    browser.find_element(*MainPage.LOGO_OPENCART)
    browser.find_element(*MainPage.NAVBAR_ITEMS)
    browser.find_element(*MainPage.SLIDER)
    browser.find_element(*MainPage.FEATURED_ITEMS)


@pytest.mark.main
@pytest.mark.parametrize('carousel_logos', [MainPage.LOGO_SONY, MainPage.LOGO_CANON,
                                            MainPage.LOGO_DELL, MainPage.LOGO_DISNEY],
                         ids=['sony', 'canon', 'dell', 'disney'])
def test_auto_swiper_carousel(base_url, browser, carousel_logos):
    browser.get(base_url)
    WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located(carousel_logos)
    )


@pytest.mark.main
def test_navbar(base_url, browser):
    browser.get(base_url)
    navbar_items = browser.find_elements(*MainPage.NAVBAR_ITEMS)
    assert len(navbar_items) == 8, "Should be 8 categories in horizontal navbar"


@pytest.mark.main
def test_featured_items(base_url, browser):
    browser.get(base_url)
    featured_items = browser.find_elements(*MainPage.FEATURED_ITEMS)
    assert len(featured_items) == 4, "Should be 4 products in Featured"


@pytest.mark.product
@pytest.mark.parametrize('product_url', ProductPage.PRODUCTS_PAGE_URL)
def test_product_page_elements(base_url, browser, product_url):
    browser.get(base_url + product_url)
    browser.find_element(*ProductPage.BREADCRUMB_ITEMS)
    browser.find_element(*ProductPage.PRODUCT_NAME)
    browser.find_element(*ProductPage.PRODUCT_PRICE)
    browser.find_element(*ProductPage.BTN_ADDED_CART)
    browser.find_element(*ProductPage.PRODUCT_IMAGES)
    browser.find_element(*ProductPage.PRODUCT_NAV)


@pytest.mark.product
@pytest.mark.parametrize('product_url', ProductPage.PRODUCTS_PAGE_URL)
def test_product_name(base_url, browser, product_url):
    browser.get(base_url + product_url)
    product_name = browser.find_element(*ProductPage.PRODUCT_NAME)
    breadcrumbs = browser.find_elements(*ProductPage.BREADCRUMB_ITEMS)
    assert breadcrumbs[-1].text == product_name.text, \
        'Product name is not the same in product card`s breadcrumbs'


@pytest.mark.product
@pytest.mark.parametrize('product_url', ProductPage.PRODUCTS_PAGE_URL)
def test_product_added_cart(base_url, browser, product_url):
    browser.get(base_url + product_url)
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(ProductPage.BTN_ADDED_CART))


@pytest.mark.login
def test_login_page_elements(admin_login_url, browser):
    browser.get(admin_login_url)
    browser.find_element(*AdminLoginPage.USERNAME_INPUT)
    browser.find_element(*AdminLoginPage.PASSWORD_INPUT)
    browser.find_element(*AdminLoginPage.LOGIN_BUTTON)
    browser.find_element(*AdminLoginPage.FORGOTTEN_PASSWORD)
    browser.find_element(*AdminLoginPage.OPENCART_LINK)


@pytest.mark.register
def test_register_page_elements(account_register_url, browser):
    try:
        browser.get(account_register_url)
        browser.find_element(*RegisterPage.FIRST_NAME_INPUT)
        browser.find_element(*RegisterPage.LAST_NAME_INPUT)
        browser.find_element(*RegisterPage.EMAIL_INPUT)
        browser.find_element(*RegisterPage.TELEPHONE_INPUT)
        browser.find_element(*RegisterPage.PASSWORD_INPUT)
        browser.find_element(*RegisterPage.PASSWORD_CONFIRM_INPUT)
        browser.find_element(*RegisterPage.DEFAULT_SUBSCRIBE)
        browser.find_element(*RegisterPage.LOGIN_PAGE_LINK).click()
    except UnexpectedAlertPresentException:
        pass


@pytest.mark.catalog
@pytest.mark.parametrize('catalog_url', CatalogPage.CATALOGS_PAGE_URL)
def test_catalog_page_elements(base_url, catalog_url, browser):
    browser.get(base_url + catalog_url)
    browser.find_element(*CatalogPage.BREADCRUMB_ITEMS)
    browser.find_element(*CatalogPage.CATALOG_NAME)
    browser.find_element(*CatalogPage.SIDEBAR)
    browser.find_element(*CatalogPage.SORT)
    browser.find_element(*CatalogPage.CATALOG_PRODUCT)
