import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BROWSERSTACK_URL = 'https://testtesttt3:fQxpEm9yH75eUKrShdz7@hub-cloud.browserstack.com/wd/hub'

desired_cap = {

  'browser': 'Safari',
 'browser_version': '13.0',
 'os': 'OS X',
 'os_version': 'Catalina',
 'resolution': '1024x768',
 'name': 'safari test testtt3est'
 }

@pytest.fixture
def remote(request):
    br =  webdriver.Remote(command_executor=BROWSERSTACK_URL,desired_capabilities=desired_cap)
    br.maximize_window()
    request.addfinalizer(wd.quit)
    return br


