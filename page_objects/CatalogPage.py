from selenium.webdriver.common.by import By

class CatalogPage:

    def __init__(self, driver, tim):
        self.tim = tim
        self.driver = driver
        self.base_url = "https://demo.opencart.com/index.php?route=product/category&path=24"

    def go_site(self):
        return self.driver.get(self.base_url)

    BUTTON_LIST = "button[data-original-title=List]"
    SORT = "input-sort"
    LIMIT = "input-limit"
    COMPARE = "compare-total"
    CONTENT_NAME = "h2"


    def button(self):
        self.driver.find_element_by_css_selector(self.BUTTON_LIST)

    def sort(self):
        self.driver.find_element_by_id(self.SORT)  # поле выбора сортировки

    def limit(self):
        self.driver.find_element_by_id(self.LIMIT)  # поле выбора количества отображаемых результатов на странице

    def compare(self):
        self.driver.find_element_by_id(self.COMPARE)  # Product Compare

    def content_name(self):
        self.driver.find_element(By.TAG_NAME, self.CONTENT_NAME)

    def close(self):
        self.driver.close()