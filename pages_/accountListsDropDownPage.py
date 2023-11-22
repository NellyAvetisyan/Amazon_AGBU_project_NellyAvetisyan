from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class AccountListDropDownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__signOutLocator = (By.ID, "nav-item-signout")

    def click_to_sign_out_button(self):
        signOutButtonElement = self._find_element(self.__signOutLocator)
        self._click(signOutButtonElement)

