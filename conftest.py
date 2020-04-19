import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="This is browser", required=True)


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

