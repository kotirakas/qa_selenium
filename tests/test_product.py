from selenium.webdriver.common.alert import Alert
from page_objects import ProductPage
import time


def test_add(browser):
    ProductPage(browser).go_site()
    ProductPage(browser).login()
    before = ProductPage(browser).list()
    ProductPage(browser).add()
    ProductPage(browser).add_product_name()
    ProductPage(browser).add_meta_name()
    ProductPage(browser).data_page()
    ProductPage(browser).add_model()
    ProductPage(browser).image_page()
    ProductPage(browser).logo_edit()
    time.sleep(5)
    ProductPage(browser).logo_download()
    time.sleep(5)
    ProductPage(browser).add_logo()
    ProductPage(browser).add_device()
    time.sleep(3)
    after = ProductPage(browser).list()
    assert after == before + 1
    browser.close()


def test_change(browser):
    ProductPage(browser).go_site()
    ProductPage(browser).login()
    before = ProductPage(browser).element()
    ProductPage(browser).edit_product()
    ProductPage(browser).add_new_name()
    ProductPage(browser).add_device()
    after = ProductPage(browser).element()
    assert before != after
    browser.close()


def test_delete(browser):
    ProductPage(browser).go_site()
    ProductPage(browser).login()
    before = ProductPage(browser).list()
    ProductPage(browser).checkbox()
    ProductPage(browser).delete()
    Alert(browser).accept()
    time.sleep(3)
    after = ProductPage(browser).list()
    assert after == before - 1
    browser.close()
