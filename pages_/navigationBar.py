from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__cartButtonElementLocator = (By.ID, "nav-cart-text-container")
        self.__searchFieldElementLocator = (By.ID, "twotabsearchtextbox")
        self.__searchSubmitButtonLocator = (By.ID, "nav-search-submit-button")
        self.__allButtonElementLocator = (By.ID, "nav-hamburger-menu")
        self.__bestSellersButtonElementLocator = (By.XPATH, "(//a[@class='hmenu-item'])[1]")
        self.__cartCountNumberElementLocator = (By.ID, "nav-cart-count")


    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonElementLocator)
        self._click(cartButtonElement)

    def fill_search_field(self, product):
        searchFieldElement = self._find_element(self.__searchFieldElementLocator)
        self._fill_field(searchFieldElement, product)

    def click_to_search_submit_button(self):
        searchSubmitButton = self._find_element(self.__searchSubmitButtonLocator)
        self._click(searchSubmitButton)

    def click_to_all_button(self):
        allButtonElement = self._find_element(self.__allButtonElementLocator)
        self._click(allButtonElement)

    def click_to_best_sellers_button(self):
        bestSellersButtonElement = self._find_element(self.__bestSellersButtonElementLocator)
        self._click(bestSellersButtonElement)

    def cart_count_element_text(self):
        cartCountNumber = self._find_element(self.__cartCountNumberElementLocator)
        self._get_element_text(cartCountNumber)
