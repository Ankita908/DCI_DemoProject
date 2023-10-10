import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    baseurl = "http://10.1.132.19/#/map-view"
    driver = webdriver.Chrome()
    driver.get(baseurl)
    driver.maximize_window()
    return driver




