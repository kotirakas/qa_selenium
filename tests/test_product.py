""" поиск элементов на страницу продукта"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from locators import ProductPage


def test_add_product_page(browser):
    """ поиск элементов на странице с возможностью выбора браузера"""
    if browser == "Chrome":
        page_test = webdriver.Chrome()
    elif browser == "Firefox":
        page_test = webdriver.Firefox()

    page_test.get("https://192.168.0.106/opencart/admin")