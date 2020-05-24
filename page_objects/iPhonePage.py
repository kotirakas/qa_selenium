import allure
class iPhonePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://192.168.0.102/opencart/index.php?route=product/product&path=24&product_id=40"

    def go_site(self):
        with allure.step(f"перехожу на адрес {self.base_url}"):
            return self.driver.get(self.base_url)

    ADD_TO_CART = "button#button-cart"
    CART_NAME = "Add to Cart"
    DEVICE_NAME = "#content > div:nth-child(1) > div.col-sm-4 > h1"
    NAME = "iPhone"
    BRAND_NAME = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(1)"
    BRAND = "Brands Apple"
    PRODUCT_CODE = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(2)"
    CODE = "Product Code: product 11"
    AVAILABILITY_STATUS = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(3)"
    STATUS = "Availability: In Stock"

    def add_to_cart(self):
        with allure.step(f"Проверяю название кнопки {self.ADD_TO_CART}"):
            name_button = self.driver.find_element_by_css_selector(self.ADD_TO_CART).text
            return name_button

    def device_name(self):
        with allure.step("проверяю  название устройства"):
            device_name = self.driver.find_element_by_css_selector(self.DEVICE_NAME).text
            return device_name

    def brand_name(self):
        with allure.step("проверяю бренд устройства"):
            brand_name = self.driver.find_element_by_css_selector(self.BRAND_NAME).text
            return brand_name

    def product_code(self):
        with allure.step("проверяю код устройства"):
            product_code = self.driver.find_element_by_css_selector(self.PRODUCT_CODE).text
            return product_code

    def availability_status(self):
        with allure.step("Проверяю доступность устройства"):
            status = self.driver.find_element_by_css_selector(self.AVAILABILITY_STATUS).text
            return status

    def close(self):
        with allure.step("Закрываю браузер"):
            self.driver.close()
