import time


class LoginPageLocators:
    LOGIN_PAGE_URL = ('https://www.saucedemo.com/')
    USERNAME = ('xpath', "//input[@id='user-name']")
    PASSWORD = ('xpath', "//input[@id='password']")
    LOGIN_BTN = ('xpath', "//input[@id='login-button']")
    LOGIN_ERROR = ('xpath', "//h3")


class MainPageLocators:
    MAIN_PAGE_URL = (f'{LoginPageLocators.LOGIN_PAGE_URL}inventory.html')

