from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    LOGO_OPENCART = (By.CSS_SELECTOR, '#logo')
    NAVBAR_ITEMS = (By.CSS_SELECTOR, ".nav > li")
    SLIDER = (By.CSS_SELECTOR, ".carousel-inner")
    FEATURED_ITEMS = (By.CSS_SELECTOR, ".product-thumb")
    LOGO_SLIDER_BUTTON_FIRST = (By.CSS_SELECTOR, '#carousel-banner-1 [data-bs-slide-to="0"]')
    LOGO_SLIDER_BUTTON_SECOND = (By.CSS_SELECTOR, '#carousel-banner-1 [data-bs-slide-to="1"]')
    LOGO_SLIDER_BUTTON_THIRD = (By.CSS_SELECTOR, '#carousel-banner-1 [data-bs-slide-to="2"]')
    LOGO_DISNEY = (By.CSS_SELECTOR, '#carousel-banner-1 .active [alt="Disney"]')
    LOGO_DELL = (By.CSS_SELECTOR, '##carousel-banner-1 .active [alt="Dell"]')
    LOGO_CANON = (By.CSS_SELECTOR, '#carousel-banner-1 .active [alt="Canon"]')
    LOGO_SONY = (By.CSS_SELECTOR, '#carousel-banner-1 .active [alt="Sony"]')
    LOGO_NINTENDO = (By.CSS_SELECTOR, '#carousel-banner-1 .active [alt="Nintendo"]')