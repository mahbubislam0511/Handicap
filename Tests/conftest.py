import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        selected_webdriver = webdriver.Chrome()
    if request.param == "firefox":
        selected_webdriver = webdriver.Firefox
    request.cls.driver = selected_webdriver
    yield
    selected_webdriver.close()