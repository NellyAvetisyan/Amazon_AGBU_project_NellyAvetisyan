from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from selenium import webdriver

class LoginPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signinButtonLocator = (By.ID, "signInSubmit")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButton = self._find_element(self.__continueButtonLocator)
        self._click(continueButton)

    def fill_password_button(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_signin_button(self):
        signinButton = self._find_element(self.__signinButtonLocator)
        self._click(signinButton)

