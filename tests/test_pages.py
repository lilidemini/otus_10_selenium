import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.CatalogPage import CatalogPage
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegisterPage import RegisterPage


@pytest.mark.main
@allure.feature('Main Page')
@allure.title('Check elements on Main Page')
@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_elements(base_url, browser):
    page = MainPage(browser)
    page.open(base_url)
    page.element(page.LOGO_OPENCART)
    page.element(page.NAVBAR_ITEMS)
    page.element(page.SLIDER)
    page.element(page.FEATURED_ITEMS)
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature('Main Page')
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title('Check logos on slider on main page')
@pytest.mark.main
@pytest.mark.parametrize('carousel_logos', [MainPage.LOGO_SONY, MainPage.LOGO_CANON,
                                            MainPage.LOGO_DELL, MainPage.LOGO_DISNEY],
                         ids=['sony', 'canon', 'dell', 'disney'])
def test_auto_swiper_carousel(base_url, browser, carousel_logos):
    page = MainPage(browser)
    page.open(base_url)
    WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located(carousel_logos)
    )
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature('Main Page')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Check count of navbar items on main page')
@pytest.mark.main
def test_navbar(base_url, browser):
    page = MainPage(browser)
    page.open(base_url)
    navbar_items = page.elements(page.NAVBAR_ITEMS)
    assert len(navbar_items) == 8, "Should be 8 categories in horizontal navbar"
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature('Main Page')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Check count of featured items on main page')
@pytest.mark.main
def test_featured_items(base_url, browser):
    page = MainPage(browser)
    page.open(base_url)
    featured_items = page.elements(page.FEATURED_ITEMS)
    assert len(featured_items) == 4, "Should be 4 products in Featured"
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature('Product Page')
@allure.title('Check elements on Product Pages: {ProductPage.PRODUCTS_PAGE_URL}')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.product
@pytest.mark.parametrize('product_url', ProductPage.PRODUCTS_PAGE_URL)
def test_product_page_elements(browser, base_url, product_url):
    product_page = ProductPage(browser)
    product_page.open(base_url + product_url)
    product_page.element(product_page.BTN_ADDED_CART)
    product_page.element(product_page.BREADCRUMB_ITEM)
    product_page.element(product_page.PRODUCT_NAME)
    product_page.element(product_page.PRODUCT_PRICE)
    product_page.elements(product_page.PRODUCT_IMAGE)
    product_page.element(product_page.PRODUCT_NAV)
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Product Page')
@allure.title(f'Check breadcrumbs of different products in pages:{ProductPage.PRODUCTS_PAGE_URL}')
@pytest.mark.product
@pytest.mark.parametrize('product_url', ProductPage.PRODUCTS_PAGE_URL)
def test_product_name(browser, base_url, product_url):
    product_page = ProductPage(browser)
    product_page.open(base_url + product_url)
    product_name = product_page.element(product_page.PRODUCT_NAME)
    breadcrumbs = product_page.elements(product_page.BREADCRUMB_ITEM)
    assert breadcrumbs[-1].text == product_name.text, \
        'Product name is not the same in product card`s breadcrumbs'
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.severity(allure.severity_level.NORMAL)
@allure.title(f'Add to a cart different products in pages:{ProductPage.PRODUCTS_PAGE_URL}')
@allure.feature('Product Page')
@pytest.mark.product
@pytest.mark.parametrize('product_url', ProductPage.PRODUCTS_PAGE_URL)
def test_product_added_cart(base_url, browser, product_url):
    product_page = ProductPage(browser)
    product_page.open(base_url + product_url)
    product_page.click(product_page.BTN_ADDED_CART)
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.title('Check elements on Admin Login Page')
@allure.feature('Admin Login Page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
def test_login_page_elements(admin_login_url, browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open(admin_login_url)
    admin_page.element(admin_page.USERNAME_INPUT)
    admin_page.element(admin_page.PASSWORD_INPUT)
    admin_page.element(admin_page.LOGIN_BUTTON)
    admin_page.element(admin_page.FORGOTTEN_PASSWORD)
    admin_page.element(admin_page.OPENCART_LINK)
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.title('Check elements on Register Page')
@allure.feature('Register Page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.register
def test_register_page_elements(account_register_url, browser):
    register_page = RegisterPage(browser)
    register_page.open(account_register_url)
    register_page.element(register_page.FIRST_NAME_INPUT)
    register_page.element(register_page.LAST_NAME_INPUT)
    register_page.element(register_page.EMAIL_INPUT)
    register_page.element(register_page.PASSWORD_INPUT)
    register_page.element(register_page.DEFAULT_SUBSCRIBE)
    register_page.click(register_page.LOGIN_PAGE_LINK)
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature('CatalogPage')
@allure.title('Check elements on CatalogPage')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.catalog
@pytest.mark.parametrize('catalog_url', CatalogPage.CATALOGS_PAGE_URL)
def test_catalog_page_elements(base_url, catalog_url, browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open(base_url + catalog_url)
    catalog_page.element(catalog_page.BREADCRUMB_ITEMS)
    catalog_page.element(catalog_page.CATALOG_NAME)
    catalog_page.element(catalog_page.SIDEBAR)
    catalog_page.element(catalog_page.SORT)
    catalog_page.element(catalog_page.CATALOG_PRODUCT)
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )
