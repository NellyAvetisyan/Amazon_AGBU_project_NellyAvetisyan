from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class SelectedProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonElementLocator = (By.ID, "add-to-cart-button")

    def click_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.__addToCartButtonElementLocator)
        self._click(addToCartButtonElement)
