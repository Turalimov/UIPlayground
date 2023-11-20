import time
from UIPlayground.locators.locators import LoginPageLocators
from UIPlayground.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.USERNAME).send_keys('standard_user')
        self.element_is_visible(self.locators.PASSWORD).send_keys('secret_sauce')
        self.element_is_clickable(self.locators.LOGIN_BTN).click()

    def fill_login_invalid(self):
        self.element_is_visible(self.locators.USERNAME).send_keys('user')
        self.element_is_visible(self.locators.PASSWORD).send_keys('secret_sauce')
        self.element_is_clickable(self.locators.LOGIN_BTN).click()
        self.element_is_present(self.locators.LOGIN_ERROR)
