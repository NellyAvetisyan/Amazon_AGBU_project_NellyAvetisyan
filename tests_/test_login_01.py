from pages_.loginPage import LoginPage
from time import sleep
from testData_.testData import validUser, userWithInvalidPassword, userWithInvalidUsername
from tests_.baseTest import BaseTest


class LogIn(BaseTest):
    def test_01_positive_login(self):
        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field(validUser.username)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        sleep(6)  # to avoid CAPTCHA check
        loginPageObj.click_to_signin_button()
        sleep(20)  # To get the title of opened page

        self.assertEqual(self.driver.title, 'Amazon.com. Spend less. Smile more.')

    def test_01_negative_login(self):
        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field(userWithInvalidPassword.username)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(userWithInvalidPassword.password)
        loginPageObj.click_to_signin_button()
        sleep(20)

        # self.assertEqual(self.driver.title, "Amazon Sign-In")
        invalidPasswordMessage = loginPageObj.get_text_of_invalid_password_message()
        self.assertEqual(invalidPasswordMessage, "Your password is incorrect")

    def test_02_negative_login(self):
        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field(userWithInvalidUsername.username)
        loginPageObj.click_to_continue_button()
        sleep(10)  # to be able to get the text locator

        invalidUsernameMessage = loginPageObj.get_text_of_invalid_username_message()
        self.assertEqual(invalidUsernameMessage, "We cannot find an account with that email address")
        # print("There was a problem. We cannot find an account with that email address/mobile number")

