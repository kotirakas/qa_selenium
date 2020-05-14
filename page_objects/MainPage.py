from selenium.webdriver.common.by import By


class MainPage:
    FEATURED = "h3"
    FIRST_CARUSEL = "slideshow0"
    LOGO_CARUSEl = "carousel0"
    PAGE_CARUSEL = "swiper-pagination.carousel0"
    CONTENT = "content"

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com"

    def go_site(self):
        return self.driver.get(self.base_url)

    def featured(self):
        fea = self.driver.find_element_by_tag_name(self.FEATURED).text
        return fea

    def first_carusel(self):
        self.driver.find_element_by_id(self.FIRST_CARUSEL)  # первая карусель

    def logo_carusel(self):
        self.driver.find_element_by_id(self.LOGO_CARUSEl)  # карусель логотипов

    def page_carusel(self):
        self.driver.find_element_by_class_name(self.PAGE_CARUSEL)  # страницы карусели логотипов

    def content(self):
        self.driver.find_element(By.ID, self.CONTENT)

    def close(self):
        self.driver.quit()
