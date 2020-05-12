import pytest
from selenium import webdriver


def pytest_addoption(parser):
     parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "opera", "yandex"])
     parser.addoption("--executor", action="store", default="192.168.0.106")

@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    return driver


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    driver = webdriver.Remote(command_executor=f"{executor}:4444/wd/hub", desired_capabilities={"browserName": browser})
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
