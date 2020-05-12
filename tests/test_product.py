from selenium.webdriver.common.alert import Alert
from page_objects import ProductPage
import time


def test_add(remote):
    ProductPage(remote).go_site()
    ProductPage(remote).login()
    before = ProductPage(remote).list()
    ProductPage(remote).add()
    ProductPage(remote).add_product_name()
    ProductPage(remote).add_meta_name()
    ProductPage(remote).data_page()
    ProductPage(remote).add_model()
    ProductPage(remote).image_page()
    ProductPage(remote).logo_edit()
    time.sleep(5)
    ProductPage(remote).logo_download()
    time.sleep(5)
    ProductPage(remote).add_logo()
    ProductPage(remote).add_device()
    time.sleep(3)
    after = ProductPage(remote).list()
    assert after == before + 1
    remote.close()


def test_change(remote):
    ProductPage(remote).go_site()
    ProductPage(remote).login()
    before = ProductPage(remote).element()
    ProductPage(remote).edit_product()
    ProductPage(remote).add_new_name()
    ProductPage(remote).add_device()
    after = ProductPage(remote).element()
    assert before != after
    remote.close()


def test_delete(remote):
    ProductPage(remote).go_site()
    ProductPage(remote).login()
    before = ProductPage(remote).list()
    ProductPage(remote).checkbox()
    ProductPage(remote).delete()
    Alert(remote).accept()
    time.sleep(3)
    after = ProductPage(remote).list()
    assert after == before - 1
    remote.close()
