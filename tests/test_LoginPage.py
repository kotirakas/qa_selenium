from locators import LoginPage
from selenium import webdriver

def test_adminlogin_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/admin/")
    br.find_element_by_css_selector(LoginPage.LOGIN_BUTTON) #кнопка логин
    br.find_element_by_css_selector(LoginPage.USERNAME) #поле ввода логина
    br.find_element_by_css_selector(LoginPage.PASSWORD) # поле ввода пвроля
    br.find_element_by_link_text(LoginPage.FORGOT_PASSWORD) #ссылка "забыл пароль#
    br.find_element_by_tag_name(LoginPage.PAGE_TEXT) #поле Please enter your login details.
    br.quit()