from selenium import webdriver

def test_good_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    br.find_element_by_link_text("Description") #Description
    br.find_element_by_id("button-cart") #add to cart
    br.find_element_by_css_selector("input[name=quantity]") #поле вввода количества
    br.find_element_by_link_text("Write a review") #ссылка "Write a review"
    br.find_element_by_css_selector(".list-unstyled h2") #цена продукта
    br.quit()