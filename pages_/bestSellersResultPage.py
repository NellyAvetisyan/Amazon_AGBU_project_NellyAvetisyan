from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class BestSellersResultPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.__bestSellersFirstProductElementLocator = (By.XPATH, "(//div[@class='has-ive-video'])[1]")


    def click_to_first_product(self):
        # bestSellersFirstProductElement = self._find_element(By.XPATH, "(//div[@class='has-ive-video'])[1]")
        bestSellersFirstProductElement = self._find_element(*self.__bestSellersFirstProductElementLocator)
        self._click(bestSellersFirstProductElement)