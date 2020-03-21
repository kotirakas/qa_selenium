from selenium import webdriver

def test_catalog_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/index.php?route=product/category&path=24")
    br.find_element_by_css_selector("button[data-original-title=List]") #кнопка List
    br.find_element_by_id("input-sort") #поле выбора сортировки
    br.find_element_by_id("input-limit") #поле выбора количества отображаемых результатов на странице
    br.find_element_by_id("compare-total") #Product Compare
    br.find_element_by_tag_name("h2") #название категории
    br.quit()