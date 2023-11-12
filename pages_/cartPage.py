from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")

    def delete_first_product(self):
        firstProductDeleteButton = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click(firstProductDeleteButton)

