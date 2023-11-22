from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from selenium import webdriver
from common_.utilities_.customLogger import logger


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signinButtonLocator = (By.ID, "signInSubmit")
        self.__invalidUsernameMassageLocator = (By.CLASS_NAME, "a-list-item")
        self.__invalidPasswordMassageLocator = (By.CLASS_NAME, "a-list-item")
        self.__needHelpDropDownButtonLocator = (By.ID, "a-expander-prompt")
        self.__forgotYourPasswordButtonLocator = (By.ID, "auth-fpp-link-bottom")
        self.__otherIssuesWithSigninLocator = (By.ID, "ap-other-signin-issues-link")
        self.__createYourAmazonAccountButtonLocator = (By.ID, "createAccountSubmit")
        self.__captchaCheckFieldLocator = (By.NAME, "cvf_captcha_input")
        self.__captchaCheckFieldContinueButtonLocator = (By.ID, "a-autoid-0-announce")
        self.__signInTextLocator = (By.CLASS_NAME, "a-spacing-small")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_signin_button(self):
        signinButtonElement = self._find_element(self.__signinButtonLocator)
        self._click(signinButtonElement)

    def get_text_of_invalid_password_message(self):
        invalidPasswordMessageElement = self._find_element(self.__invalidPasswordMassageLocator)
        return self._get_element_text(invalidPasswordMessageElement)

    def get_text_of_invalid_username_message(self):
        invalidUsernameMassageElement = self._find_element(self.__invalidUsernameMassageLocator)
        return self._get_element_text(invalidUsernameMassageElement)
    logger("INFO", "There was a problem. We cannot find an account with that email address/mobile number")

    def click_to_need_help_drop_down_button(self):
        needHelpDropDownButtonElement = self._find_element(self.__needHelpDropDownButtonLocator)
        self._click(needHelpDropDownButtonElement)

    def click_to_forgot_your_password_button(self):
        forgotYourPasswordButtonElement = self._find_element(self.__forgotYourPasswordButtonLocator)
        self._click(forgotYourPasswordButtonElement)

    def click_to_other_issues_with_signin(self):
        otherIssuesWithSigninElement = self._find_element(self.__otherIssuesWithSigninLocator)
        self._click(otherIssuesWithSigninElement)

    def click_to_create_your_amazon_account_button(self):
        createYourAmazonAccountButton = self._find_element(self.__createYourAmazonAccountButtonLocator)
        self._click(createYourAmazonAccountButton)

    def fill_captcha_check_field(self):
        captchaCheckField = self._find_element(self.__captchaCheckFieldLocator)
        self._click(captchaCheckField)

    def click_to_continue_button_in_captcha_check_page(self):
        continueButtonInCaptchaCheckPage = self._find_element(self.__captchaCheckFieldContinueButtonLocator)
        self._click(continueButtonInCaptchaCheckPage)

    def get_sign_in_text(self):
        signInTextElement = self._find_element(self.__signInTextLocator)
        return self._get_element_text(signInTextElement)
