import time

import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser,url):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
