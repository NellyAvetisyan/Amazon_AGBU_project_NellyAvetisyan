from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class HamburgMenuLeftSideOpenedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__bestSellersButtonLocator = (By.XPATH, "(//a[@class='hmenu-item'])[1]")

    def click_to_best_sellers_button(self):
        bestSellersButtonElement = self._find_element(self.__bestSellersButtonLocator)
        self._click(bestSellersButtonElement)
