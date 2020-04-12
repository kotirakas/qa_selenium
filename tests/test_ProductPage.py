""" поиск элементов на страницу продукта"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from locators import ProductPage


def test_product_page(browser, tim):
    """ поиск элементов на странице с возможностью выбора браузера"""
    if browser == "Chrome":
        page_test = webdriver.Chrome()
    elif browser == "Firefox":
        page_test = webdriver.Firefox()

    page_test.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(page_test, tim)
    try:
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, ProductPage.DESCRIPTION)))
        wait.until(EC.presence_of_element_located((By.ID, ProductPage.ADD)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ProductPage.QUANTITY)))
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, ProductPage.REVIEW)))
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ProductPage.PRICE)))
    except NoSuchElementException:
        print("нет такого элемента")
    except TimeoutException:
        print("time is over")
    finally:
        page_test.quit()
