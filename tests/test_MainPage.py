from locators import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_mainpage(browser):
    if browser == "Chrome":
        br = webdriver.Chrome()
    elif browser == "Firefox":
        br = webdriver.Firefox()
    br.get("https://demo.opencart.com")
    fea = br.find_element_by_tag_name(MainPage.FEATURED)
    assert fea.text == "Featured"
    br.find_element_by_id(MainPage.FIRST_CARUSEL) #первая карусель
    br.find_element_by_id(MainPage.LOGO_CARUSEl) #карусель логотипов
    br.find_element_by_class_name(MainPage.PAGE_CARUSEL) #страницы карусели логотипов
    br.find_element(By.ID, MainPage.CONTENT)
    br.quit()


