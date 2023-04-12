from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOGO_OPENCART = (By.CSS_SELECTOR, '#logo')
    NAVBAR_ITEMS = (By.CSS_SELECTOR, ".nav > li")
    SLIDER = (By.CSS_SELECTOR, "#carousel-banner-0 .carousel-inner")
    FEATURED_ITEMS = (By.CSS_SELECTOR, ".product-thumb")
    LOGO_DISNEY = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Disney"]')
    LOGO_DELL = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Dell"]')
    LOGO_CANON = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Canon"]')
    LOGO_SONY = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Sony"]')
    LOGO_NINTENDO = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center.swiper-slide-active [alt="Nintendo"]')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "form .dropdown")
    CURRENCY_EURO = (By.CSS_SELECTOR, "ul.show > li:nth-child(1) > a.dropdown-item")
    CURRENCY_GBR = (By.CSS_SELECTOR, "ul.show > li:nth-child(2) > a.dropdown-item")
    CURRENCY_USD = (By.CSS_SELECTOR, "ul.show > li:nth-child(3) > a.dropdown-item")
    CURRENT_CURRENCY_ICON = (By.CSS_SELECTOR, "a > strong")

    def open_main_page(self, url):
        self.browser.get(url)
        return self

    def check_elements_on_page(self):
        self.element(self.CURRENCY_DROPDOWN)
        self.element(self.LOGO_OPENCART)
        self.element(self.SLIDER)
        self.element(self.FEATURED_ITEMS)
        return self

    def change_currency(self, currency):
        self.click_element(self.element(self.CURRENCY_DROPDOWN))
        self.click_element(self.element(currency))
        return self

    def check_current_currency(self, current_currency):
        assert self.get_element_text(self.CURRENT_CURRENCY_ICON) == current_currency
