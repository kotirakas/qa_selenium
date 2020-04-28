from selenium import webdriver


class SearchPage:
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com/index.php?route=product/search&search=htc")
    CONTENT_NAME = "#content h1"
    INPUT_SEARCH = "input-search"
    CATEGORY = "select[name=category_id]"
    LIMIT = "#input-limit"
    COMPARE = "compare-total"

    def search_name(self):
        search_name = self.browser.find_element_by_css_selector(self.CONTENT_NAME).text
        return search_name

    # assert search_name.text == "Search - htc"

    def input_search(self):
        self.browser.find_element_by_id(self.INPUT_SEARCH)  # поле ввода запроса

    def category(self):
        self.browser.find_element_by_css_selector(self.CATEGORY)  # кнопка выбора категорий

    def limit(self):
        self.browser.find_element_by_css_selector(self.LIMIT)  # кол-во показываемых единиц

    def compare(self):
        self.browser.find_element_by_id(self.COMPARE)  # Product Compare

    def close(self):
        self.browser.quit()
