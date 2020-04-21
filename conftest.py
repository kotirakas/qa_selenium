import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="This is browser", required=True)
    #parser.addoption("--url", "-U", action="store", default="http://192.168.0.106/opencart/admin/index.php?route=catalog/product", help="choose your browser")
@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    #driver.implicitly_wait(20)
    driver.get("http://192.168.0.106/opencart/admin/index.php?route=catalog/product")
    driver.find_element_by_id("input-username").send_keys("admin")
    driver.find_element_by_id("input-password").send_keys("admin")
    driver.find_element_by_tag_name("button").click()


    return driver

