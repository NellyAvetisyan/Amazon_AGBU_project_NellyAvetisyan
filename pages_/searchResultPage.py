from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def click_to_first_product(self):
        firstProductElement = self._find_element(By.XPATH, "(//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'])[1]")
        self._click(firstProductElement)
