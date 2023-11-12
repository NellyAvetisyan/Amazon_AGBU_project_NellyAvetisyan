import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.bestSellersResultPage import BestSellersResultPage
from pages_.selectedProductPage import SelectedProductPage
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener

class TestAllSteps(unittest.TestCase):

    def setUp(self):
        self.simpledriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpledriver, MyListener())
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        sleep(10)  # to avoid checking message

        loginPageObj = LoginPage(self.simpledriver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_button("Korea2022")
        sleep(10)  # to avoid CAPTCHA check
        loginPageObj.click_signin_button()

    def test_add_to_cart_from_best_sellers_first_product(self):
        navigationBarObj = NavigationBar(self.simpledriver)
        navigationBarObj.click_to_all_button()
        navigationBarObj.click_to_best_sellers_button()

        bestSellersResultPageObj = BestSellersResultPage(self.simpledriver)
        bestSellersResultPageObj.click_to_first_product()

        selectedProductPageObj = SelectedProductPage(self.simpledriver)
        selectedProductPageObj.click_add_to_cart_button()
        sleep(10)  # to see the action

        # cartCountNumber = int(navigationBarObj.cart_count_element_text())
        # self.assertEqual(cartCountNumber, cartCountNumber + 1)

    def tearDown(self):
        self.driver.close()




