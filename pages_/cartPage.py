from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")
        self.__cartCountNumberLocator = (By.ID, "nav-cart-count")
        self.__emptyCartMessageLocator = (By.CLASS_NAME, "a-spacing-mini.a-spacing-top-base")



    def get_cart_count(self):
        cartCountityElement = self._find_element(self.__cartCountNumberLocator)
        return int(self._get_element_text(cartCountityElement))

    def delete_first_product_from_cart(self):
        firstProductDeleteButton = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click(firstProductDeleteButton)
        # cartCountNumberElement = self.get_text_of_cart_count_number()
        # if cartCountNumberElement == 0:
        #     print("WARNING: Your Amazon Cart is empty.")
        #     pass
        # else:
        #     firstProductDeleteButton = self._find_element(self.__firstProductDeleteButtonLocator)
        #     self._click(firstProductDeleteButton)

    def get_text_of_empty_cart_message(self):
        emptyCartMessageElement = self._find_element(self.__emptyCartMessageLocator)
        return self._get_element_text(emptyCartMessageElement)

    def delete_all_products_from_cart(self):
        cartCountNumberElement = self.get_cart_count()
        while self.get_cart_count() != 0:
            self.delete_first_product_from_cart()
            cartCountNumberElement -= 1
            # self.get_cart_count() -= 1
        # else:
        #     print("Your cart is already empty")
        #     pass

