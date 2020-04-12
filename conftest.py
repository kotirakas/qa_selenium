import pytest


def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default=10, help="This is timeout", required=False)
    parser.addoption("--browser", action="store", default="Chrome", help="This is browser", required=True)



@pytest.fixture
def tim(request):
    return int(request.config.getoption("--timeout"))


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

