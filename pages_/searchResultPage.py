from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductElementLocator = (By.XPATH, "(//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'])[1]")

    def click_to_first_product(self):
        # firstProductElement = self._find_element(By.XPATH, "(//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'])[1]")
        firstProductElement = self._find_element(*self.__firstProductElementLocator)
        self._click(firstProductElement)
