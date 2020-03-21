from selenium import webdriver
from locators import ProductPage

def test_product_page():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    br.find_element_by_link_text(ProductPage.DESCRIPTION) #Description
    br.find_element_by_id(ProductPage.ADD) #add to cart
    br.find_element_by_css_selector(ProductPage.QUANTITY) #поле вввода количества
    br.find_element_by_link_text(ProductPage.REVIEW) #ссылка "Write a review"
    br.find_element_by_css_selector(ProductPage.PRICE) #цена продукта
    br.quit()