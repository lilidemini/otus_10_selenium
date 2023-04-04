from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    LOGO_OPENCART = (By.CSS_SELECTOR, '#logo')
    NAVBAR_ITEMS = (By.CSS_SELECTOR, ".nav > li")
    SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    FEATURED_ITEMS = (By.CSS_SELECTOR, ".product-thumb")
    LOGO_DISNEY = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Disney"]')
    LOGO_DELL = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Dell"]')
    LOGO_CANON = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Canon"]')
    LOGO_SONY = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Sony"]')
    LOGO_NINTENDO = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Nintendo"]')
