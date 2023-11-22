from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-text-container")
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchSubmitButtonLocator = (By.ID, "nav-search-submit-button")
        self.__allHamburgMenuButtonLocator = (By.ID, "nav-hamburger-menu")
        self.__deliverToButtonLocator = (By.ID, "glow-ingress-block")
        self.__languageChangeButtonLocator = (By.CLASS_NAME, "icp-nav-link-inner")
        self.__accountAndListButtonLocator = (By.ID, "nav-link-accountList")
        self.__cartCountLocator = (By.ID, "nav-cart-count")

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)

    def fill_search_field(self, product):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, product)

    def click_to_search_submit_button(self):
        searchSubmitButtonElement = self._find_element(self.__searchSubmitButtonLocator)
        self._click(searchSubmitButtonElement)

    def click_to_all_hamburg_menu_button(self):
        allHamburgMenuButtonElement = self._find_element(self.__allHamburgMenuButtonLocator)
        self._click(allHamburgMenuButtonElement)

    def get_cart_count(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        return int(self._get_element_text(cartCountElement))

    def click_to_deliver_to_button(self):
        deliverToButtonElement = self._find_element(self.__deliverToButtonLocator)
        self._click(deliverToButtonElement)

    def move_to_language_change_button(self):
        languageChangeButtonElement = self._find_element(self.__languageChangeButtonLocator)
        self._mouse_move(languageChangeButtonElement)

    def move_to_account_and_lists_button(self):
        accountAndListButtonElement = self._find_element(self.__accountAndListButtonLocator)
        self._mouse_move(accountAndListButtonElement)

