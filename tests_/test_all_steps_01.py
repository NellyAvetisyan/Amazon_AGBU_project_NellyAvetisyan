import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from pages_.searchResultPage import SearchResultPage
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

        loginPageObj = LoginPage(self.simpledriver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_button("Korea2022")
        sleep(10)  # to avoid CAPTCHA check
        loginPageObj.click_signin_button()

    def test_steps_to_check_func(self):

        navigationBarObj = NavigationBar(self.simpledriver)
        navigationBarObj.click_to_cart_button()

        cartPageObj = CartPage(self.simpledriver)
        cartPageObj.delete_first_product()

        # cartCountNumber = int(navigationBarObj.cart_count_element_text())
        # self.assertEqual(cartCountNumber, cartCountNumber - 1)

        navigationBarObj.fill_search_field("candle")
        navigationBarObj.click_to_search_submit_button()

        searchResultPaeObj = SearchResultPage(self.simpledriver)
        searchResultPaeObj.click_to_first_product()

        # self.assertEqual(self.driver.title, "Amazon.com : candles")
        # # just assertion using example, only for this product search

        selectedProductObj = SelectedProductPage(self.simpledriver)
        selectedProductObj.click_add_to_cart_button()

        # self.assertEqual(cartCountNumber, cartCountNumber + 1)

    def tearDown(self):
        self.driver.close()
