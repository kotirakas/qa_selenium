from selenium import webdriver


class ProductPage:
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    DESCRIPTION = "Description"
    ADD = "button-cart"
    QUANTITY = "input[name=quantity]"
    REVIEW = "Write a review"
    PRICE = ".list-unstyled h2"

    def description(self):
        self.browser.find_element_by_link_text(self.DESCRIPTION)  # Description

    def add(self):
        self.browser.find_element_by_id(self.ADD)  # add to cart

    def quantity(self):
        self.browser.find_element_by_css_selector(self.QUANTITY)  # поле вввода количества

    def review(self):
        self.browser.find_element_by_link_text(self.REVIEW)  # ссылка "Write a review"

    def price(self):
        self.browser.find_element_by_css_selector(self.PRICE)  # цена продукта

    def close(self):
        self.browser.quit()
