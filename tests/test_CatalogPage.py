from locators import CatalogPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_catalog_page():
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=24")
    browser.find_element_by_css_selector(CatalogPage.BUTTON_LIST) #кнопка List
    browser.find_element_by_id(CatalogPage.SORT) #поле выбора сортировки
    browser.find_element_by_id(CatalogPage.LIMIT) #поле выбора количества отображаемых результатов на странице
    browser.find_element_by_id(CatalogPage.COMPARE) #Product Compare
    browser.find_element(By.TAG_NAME, CatalogPage.CONTENT_NAME) #название категории
    browser.quit()