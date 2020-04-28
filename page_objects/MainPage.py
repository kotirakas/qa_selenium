from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:
    FEATURED = "h3"
    FIRST_CARUSEL = "slideshow0"
    LOGO_CARUSEl = "carousel0"
    PAGE_CARUSEL = "swiper-pagination.carousel0"
    CONTENT = "content"
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com")

    def featured(self):
        fea = self.browser.find_element_by_tag_name(self.FEATURED).text
        return fea

    def first_carusel(self):
        self.browser.find_element_by_id(self.FIRST_CARUSEL)  # первая карусель

    def logo_carusel(self):
        self.browser.find_element_by_id(self.LOGO_CARUSEl)  # карусель логотипов

    def page_carusel(self):
        self.browser.find_element_by_class_name(self.PAGE_CARUSEL)  # страницы карусели логотипов

    def content(self):
        self.browser.find_element(By.ID, self.CONTENT)

    def close(self):
        self.browser.quit()
