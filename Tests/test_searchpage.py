from selenium import webdriver

def test_search_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/index.php?route=product/search&search=htc")
    br.find_element_by_css_selector("#content h1")
    br.find_element_by_id("input-search") # поле ввода запроса
    br.find_element_by_css_selector("select[name=category_id]") #кнопка выбора категорий
    br.find_element_by_css_selector("label[for=input-limit]") #show
    br.find_element_by_id("compare-total") #Product Compare
    br.quit()