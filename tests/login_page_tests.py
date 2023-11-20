import time
from UIPlayground.pages.base_page import BasePage
from UIPlayground.conftest import driver
from UIPlayground.pages.login_page import LoginPage
from UIPlayground.locators.locators import LoginPageLocators
from UIPlayground.locators.locators import MainPageLocators

class TestLoginPage:
    def test_login_page(self, driver):
        text_login_page = LoginPage(driver, LoginPageLocators.LOGIN_PAGE_URL)
        text_login_page.open()
        text_login_page.fill_all_fields()
        current_url = driver.current_url
        time.sleep(5)
        assert current_url == MainPageLocators.MAIN_PAGE_URL, 'url is not valid'

