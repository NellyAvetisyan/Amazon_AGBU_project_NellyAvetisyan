from pages_.navigationBar import NavigationBar
from pages_.bestSellersResultPage import BestSellersResultPage
from pages_.selectedProductDetailPage import SelectedProductDetailPage
from pages_.hamburgMenuLeftSideOpenedPage import HamburgMenuLeftSideOpenedPage
from time import sleep
from tests_.baseTest import BaseTestwithLoginSteps

class TestAddToCartFromAllHamburgMenuBestSellersResultPage(BaseTestwithLoginSteps):
    def test_add_to_cart_from_best_sellers_first_product(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.click_to_all_hamburg_menu_button()
        humburgMenuLeftSideOpenedPageObj = HamburgMenuLeftSideOpenedPage(self.simpleDriver)
        humburgMenuLeftSideOpenedPageObj.click_to_best_sellers_button()

        bestSellersResultPageObj = BestSellersResultPage(self.simpleDriver)
        bestSellersResultPageObj.click_to_first_product()

        cartCountNumberbeforeAddingToCart = navigationBarObj.get_cart_count()
        selectedProductPageObj = SelectedProductDetailPage(self.simpleDriver)
        selectedProductPageObj.click_add_to_cart_button()
        cartCountNumberAfterAddingToCart = navigationBarObj.get_cart_count()
        sleep(10)  # to see the action


        self.assertEqual(cartCountNumberAfterAddingToCart, cartCountNumberbeforeAddingToCart + 1)

