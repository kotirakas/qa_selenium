import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default=10, help="This is timeout", required=False)
    parser.addoption("--browser", action="store", default="Chrome", help="This is browser", required=True)



@pytest.fixture
def tim(request):
    return int(request.config.getoption("--timeout"))


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()

    return driver

