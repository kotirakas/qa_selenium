import pytest
from selenium import webdriver


def pytest_addoption(parser):
     parser.addoption("--browser", action="store", default="chrome")
     #parser.addoption("--selenoid", action="store", default="True")

@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    return driver


#@pytest.fixture
#def remote(request):
    #browser = request.config.getoption("--browser")
    #selenoid = request.config.getoption("--selenoid")
    #if selenoid:
        #executor = "192.168.0.105"
        #driver = webdriver.Remote(command_executor=f"{executor}:4444/wd/hub", desired_capabilities={"browserName": browser,
         #"enableVNC": True, "enableVideo": True, "name": "tests selenoid"})
    #else:
     #   driver = webdriver.Chrome()
    #driver.maximize_window()
    #request.addfinalizer(driver.quit)
    #return driver
