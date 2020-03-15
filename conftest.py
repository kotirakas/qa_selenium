import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://192.168.0.108/opencart/", help="This is base url", required=True)
    parser.addoption("--browser", action="store", default="Chrome", help="This is browser", required=True)


@pytest.fixture
def url_base(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

