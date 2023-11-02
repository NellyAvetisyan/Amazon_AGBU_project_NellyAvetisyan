from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class LoginPage(BasePage):
    def fill_username_field(self,username):
        userNameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButton = self._find_element(By.ID, "continue")
        self._click(continueButton)

    def fill_password_button(self, password):
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFieldElement, password)

    def click_signin_button(self):
        signinButton = self._find_element(By.ID, "signInSubmit")
        self._click(signinButton)



