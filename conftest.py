import pytest
from selenium import webdriver
import logging
import argparse
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#parser = argparse.ArgumentParser()
#parser.add_argument("-f", "--file", default=None)
#args = parser.parse_args()

logging.basicConfig(filename="tests.log", level=logging.INFO)
logger = logging.getLogger('browser')

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        logging.info(f"I'm looking for '{value}' with '{by}'")


    def after_find(self, element, value, driver):
        logging.info(f"I've found '{value}' with '{element}'")


    def on_exception(self, exception, driver):
        logging.error(f'sorry, but i got: {exception}')
        driver.save_screenshot('error.png')


def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default=10, help="This is timeout", required=False)
    parser.addoption("--browser", action="store", default="Chrome", help="This is browser", required=True)



@pytest.fixture
def tim(request):
    return int(request.config.getoption("--timeout"))


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    logger.info('====== Started fixture ======')
    if browser_param == "chrome":
        d = DesiredCapabilities.CHROME
        opt = webdriver.ChromeOptions()
        driver = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=d, options=opt), MyListener())
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
        driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())

    request.addfinalizer(driver.quit)
    logger.info('====== Finish fixture  ======')
    return driver





