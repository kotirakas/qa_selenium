from locators import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_mainpage():
    browser = webdriver.Chrome()
    browser.get("https://demo.opencart.com")
    fea = browser.find_element_by_tag_name(MainPage.FEATURED)
    assert fea.text == "Featured"
    browser.find_element_by_id(MainPage.FIRST_CARUSEL) #первая карусель
    browser.find_element_by_id(MainPage.LOGO_CARUSEl) #карусель логотипов
    browser.find_element_by_class_name(MainPage.PAGE_CARUSEL) #страницы карусели логотипов
    browser.find_element(By.ID, MainPage.CONTENT)
    browser.quit()


