class ProductPage:
    DESCRIPTION = "Description"
    ADD = "button-cart"
    QUANTITY = "input[name=quantity]"
    REVIEW = "Write a review"
    PRICE = ".list-unstyled h2"

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"

    def go_site(self):
        return self.driver.get(self.base_url)

    def description(self):
        self.driver.find_element_by_link_text(self.DESCRIPTION)  # Description

    def add(self):
        self.driver.find_element_by_id(self.ADD)  # add to cart

    def quantity(self):
        self.driver.find_element_by_css_selector(self.QUANTITY)  # поле вввода количества

    def review(self):
        self.driver.find_element_by_link_text(self.REVIEW)  # ссылка "Write a review"

    def price(self):
        self.driver.find_element_by_css_selector(self.PRICE)  # цена продукта

    def close(self):
        self.driver.quit()
