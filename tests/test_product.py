from selenium.webdriver.common.alert import Alert
from locators import ProductPage
import time

def test_add(browser):
    before = len(browser.find_elements_by_xpath(ProductPage.LIST))
    browser.find_element_by_xpath(ProductPage.ADD).click()
    browser.find_element_by_css_selector(ProductPage.PRODUCT_NAME).send_keys(ProductPage.NAME)
    browser.find_element_by_css_selector(ProductPage.META_NAME).send_keys(ProductPage.NAME)
    browser.find_element_by_xpath(ProductPage.DATA_PAGE).click()
    browser.find_element_by_css_selector(ProductPage.MODEL_NAME).send_keys(ProductPage.MODEL)
    browser.find_element_by_css_selector(ProductPage.ADD_DEVICE).click()
    after = len(browser.find_elements_by_xpath(ProductPage.LIST))
    assert after == before + 1
    browser.close()


def test_change(browser):
    before = browser.find_element_by_xpath(ProductPage.ELEMENT).text
    browser.find_element_by_xpath(ProductPage.EDIT).click()
    browser.find_element_by_css_selector(ProductPage.PRODUCT_NAME).send_keys(ProductPage.NEW_NAME)
    browser.find_element_by_css_selector(ProductPage.ADD_DEVICE).click()
    after = browser.find_element_by_xpath(ProductPage.ELEMENT).text
    assert before != after
    browser.close()


def test_delete(browser):
    before = len(browser.find_elements_by_xpath(ProductPage.LIST))
    browser.find_element_by_xpath(ProductPage.CHECKBOX).click()
    browser.find_element_by_xpath(ProductPage.DELETE).click()
    Alert(browser).accept()
    time.sleep(3)
    after = len(browser.find_elements_by_xpath(ProductPage.LIST))
    assert after == before - 1
    browser.close()
