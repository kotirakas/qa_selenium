from locators import CatalogPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_catalog_page(browser):
    if browser == "Chrome":
        wd = webdriver.Chrome()
    elif browser == "Firefox":
        wd = webdriver.Firefox()
    wd.get("https://demo.opencart.com/index.php?route=product/category&path=24")
    wd.find_element_by_css_selector(CatalogPage.BUTTON_LIST) #кнопка List
    wd.find_element_by_id(CatalogPage.SORT) #поле выбора сортировки
    wd.find_element_by_id(CatalogPage.LIMIT) #поле выбора количества отображаемых результатов на странице
    wd.find_element_by_id(CatalogPage.COMPARE) #Product Compare
    wd.find_element(By.TAG_NAME, CatalogPage.CONTENT_NAME) #название категории
    wd.quit()