from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class SelectedProductPage(BasePage):

    def click_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(By.ID, "add-to-cart-button")
        self._click(addToCartButtonElement)
