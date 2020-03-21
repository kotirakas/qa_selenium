from selenium import webdriver
from locators import SearchPage

def test_search_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/index.php?route=product/search&search=htc")
    search_name = br.find_element_by_css_selector(SearchPage.CONTENT_NAME)
    assert search_name.text == "Search - htc"
    br.find_element_by_id(SearchPage.INPUT_SEARCH) # поле ввода запроса
    br.find_element_by_css_selector(SearchPage.CATEGORY) #кнопка выбора категорий
    br.find_element_by_css_selector(SearchPage.LIMIT) #кол-во показываемых единиц
    br.find_element_by_id(SearchPage.COMPARE) #Product Compare
    br.quit()