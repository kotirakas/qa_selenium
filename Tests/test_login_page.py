from selenium import webdriver

def test_adminlogin_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/admin/")
    br.find_element_by_css_selector("button[type=submit]") #кнопка логин
    br.find_element_by_css_selector("input#input-username") #поле ввода логина
    br.find_element_by_css_selector("input#input-password") # поле ввода пвроля
    br.find_element_by_link_text("Forgotten Password") #ссылка "забыл пароль#
    br.find_element_by_tag_name("h1") #поле Please enter your login details.
    br.quit()