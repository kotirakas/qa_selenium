from selenium import webdriver
from selenium.webdriver.common.by import By


class CatalogPage:
    BUTTON_LIST = "button[data-original-title=List]"
    SORT = "input-sort"
    LIMIT = "input-limit"
    COMPARE = "compare-total"
    CONTENT_NAME = "h2"
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=24")

    def button(self):
        self.browser.find_element_by_css_selector(self.BUTTON_LIST)

    def sort(self):
        self.browser.find_element_by_id(self.SORT)  # поле выбора сортировки

    def limit(self):
        self.browser.find_element_by_id(self.LIMIT)  # поле выбора количества отображаемых результатов на странице

    def compare(self):
        self.browser.find_element_by_id(self.COMPARE)  # Product Compare

    def content_name(self):
        self.browser.find_element(By.TAG_NAME, self.CONTENT_NAME)

    def close(self):
        self.browser.close()
