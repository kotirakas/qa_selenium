class SearchPage:
    CONTENT_NAME = "#content h1"
    INPUT_SEARCH = "input-search"
    CATEGORY = "select[name=category_id]"
    LIMIT = "#input-limit"
    COMPARE = "compare-total"

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com/index.php?route=product/search&search=htc"

    def go_site(self):
        return self.driver.get(self.base_url)

    def search_name(self):
        search_name = self.driver.find_element_by_css_selector(self.CONTENT_NAME).text
        return search_name

    def input_search(self):
        self.driver.find_element_by_id(self.INPUT_SEARCH)  # поле ввода запроса

    def category(self):
        self.driver.find_element_by_css_selector(self.CATEGORY)  # кнопка выбора категорий

    def limit(self):
        self.driver.find_element_by_css_selector(self.LIMIT)  # кол-во показываемых единиц

    def compare(self):
        self.driver.find_element_by_id(self.COMPARE)  # Product Compare

    def close(self):
        self.driver.quit()
