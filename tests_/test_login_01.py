import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from time import sleep


class LogIn(unittest.Testcase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_01_positive_login(self):
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_button("Korea2022")
        sleep(6)
        # to avoid CAPTCHA check
        loginPageObj.click_signin_button()

    def test_01_negative_login(self):
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_button("12345678")
        loginPageObj.click_signin_button()

    def tearDown(self):
        self.driver.close()
