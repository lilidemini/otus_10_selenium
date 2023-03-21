from selenium.webdriver.common.by import By

class MainPage:
    LOGO_OPENCART = (By.CSS_SELECTOR, '#logo')
    NAVBAR_ITEMS = (By.CSS_SELECTOR, ".nav > li")
    SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    FEATURED_ITEMS = (By.CSS_SELECTOR, ".product-thumb")
    LOGO_DISNEY = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Disney"]')
    LOGO_DELL = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Dell"]')
    LOGO_CANON = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Canon"]')
    LOGO_SONY = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Sony"]')
    LOGO_NINTENDO = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Nintendo"]')

class ProductPage:
    PRODUCTS_PAGE_URL = ['iphone', 'imac', 'component/monitor/samsung-syncmaster-941bw', 'camera/canon-eos-5d']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".list-unstyled h2")
    BTN_ADDED_CART = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".thumbnails")
    PRODUCT_NAV = (By.CSS_SELECTOR, 'ul.nav.nav-tabs')

class AdminLoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, 'OpenCart')

class RegisterPage:
    LOGIN_PAGE_LINK = (By.LINK_TEXT, "login page")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    DEFAULT_SUBSCRIBE = (By.CSS_SELECTOR, 'input[value="0"][checked="checked"]')

class CatalogPage:
    CATALOGS_PAGE_URL = ['desktops', 'laptop-notebook', 'tablet', 'smartphone', 'camera', 'mp3-players']
    BREADCRUMB_ITEMS = (By.CSS_SELECTOR, ".breadcrumb li")
    CATALOG_NAME = (By.CSS_SELECTOR, "h2")
    SIDEBAR = (By.CSS_SELECTOR, "#column-left")
    SORT= (By.CSS_SELECTOR, "#input-sort")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CATALOG_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
