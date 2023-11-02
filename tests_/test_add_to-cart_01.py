import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
# from pages_.cartPage import CartPage
from pages_.bestSellersResultPage import BestSellersResultPage
from pages_.selectedProductPage import SelectedProductPage
from time import sleep

class TestAllSteps(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_button("Korea2022")
        sleep(10)
        # to avoid CAPTCHA check
        loginPageObj.click_signin_button()

    def test_add_to_cart_from_best_sellers_first_product(self):
        NavigationBarObj = NavigationBar(self.driver)
        NavigationBarObj.click_to_all_button()
        NavigationBarObj.click_to_best_sellers_button()

        BestSellersResultPageObj = BestSellersResultPage(self.driver)
        BestSellersResultPageObj.click_to_first_product()

        SelectedProductPageObj = SelectedProductPage(self.driver)
        SelectedProductPageObj.click_add_to_cart_button()
        sleep(10)

        # self.assertGreater






