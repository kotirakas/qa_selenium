

from selenium import webdriver

def test_mainpage():
    br = webdriver.Chrome()
    br.get("https://demo.opencart.com")
    br.find_element_by_tag_name("h3") #Featured
    br.find_element_by_id("slideshow0") #первая карусель
    br.find_element_by_id("carousel0") #карусель логотипов
    br.find_element_by_class_name("swiper-pagination.carousel0") #страницы карусели логотипов
    br.find_element_by_css_selector(".navbar-nav") #меню
    br.quit()


