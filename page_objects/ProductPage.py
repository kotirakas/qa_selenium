from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class ProductPage:

    def __init__(self, driver, tim):
        self.tim = tim
        self.driver = driver
        self.base_url = "https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"

    def go_site(self):
        logger.info('====== Started ProductPage ======')
        return self.driver.get(self.base_url)

    DESCRIPTION = "Description"
    ADD = "button-cart"
    QUANTITY = "input[name=quantity]"
    REVIEW = "Write a review"
    PRICE = ".list-unstyled h2"

    def wait_description(self):
        return WebDriverWait(self.driver, self.tim).until(EC.presence_of_element_located((By.LINK_TEXT, self.DESCRIPTION)))

    def wait_add(self):
        return WebDriverWait(self.driver, self.tim).until(EC.presence_of_element_located((By.ID, self.ADD)))

    def wait_quantity(self):
        return WebDriverWait(self.driver, self.tim).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.QUANTITY)))

    def wait_review(self):
        return WebDriverWait(self.driver, self.tim).until(EC.presence_of_element_located((By.LINK_TEXT, self.REVIEW)))

    def wait_price(self):
        return WebDriverWait(self.driver, self.tim).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.PRICE)))

    #
    def close(self):
        logger.info('====== Closed ProductPage ======')
        self.driver.quit()
