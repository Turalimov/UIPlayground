import time
from UIPlayground.pages.base_page import BasePage
from UIPlayground.conftest import driver


def test(driver):
    page = BasePage(driver, 'https://www.saucedemo.com/')
    page.open()
    time.sleep(5)
