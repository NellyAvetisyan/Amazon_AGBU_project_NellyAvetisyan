from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBar(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(By.ID, "nav-cart-text-container")
        self._click(cartButtonElement)
