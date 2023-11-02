from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class BestSellersResultPage(BasePage):

    def click_to_first_product(self):
        bestSellersFirstProductElement = self._find_element(By.XPATH, "(//div[@class='has-ive-video'])[1]")
        self._click(bestSellersFirstProductElement)