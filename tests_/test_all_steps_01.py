from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from pages_.searchResultPage import SearchResultPage
from pages_.selectedProductDetailPage import SelectedProductDetailPage

from tests_.baseTest import BaseTestwithLoginSteps


class TestSearchingAddToCartDeleteFunctionalities(BaseTestwithLoginSteps):
    def test_search_add_to_cart_delete_product_from_cart_func(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.fill_search_field("candle")
        navigationBarObj.click_to_search_submit_button()

        searchResultPaeObj = SearchResultPage(self.simpleDriver)
        searchResultPaeObj.click_to_first_product()

        # cartNumberCountBeforeAddToCart = int(navigationBarObj.get_cart_count_element_text())
        # print(cartNumberCountBeforeAddToCart)

        selectedProductObj = SelectedProductDetailPage(self.simpleDriver)
        selectedProductObj.click_add_to_cart_button()

        # cartNumberCountAfterAddToCart = int(navigationBarObj.get_cart_count_element_text())
        # self.assertNotEqual(cartNumberCountBeforeAddToCart, cartNumberCountAfterAddToCart)


        navigationBarObj.click_to_cart_button()

        # cartNumberCountBeforeAddToCart = int(navigationBarObj.get_cart_count_element_text())

        cartPageObj = CartPage(self.simpleDriver)
        cartPageObj.delete_first_product_from_cart()

        # cartNumberCountAfterAddToCart = int(navigationBarObj.get_cart_count_element_text())
        # self.assertIs(cartNumberCountAfterAddToCart, cartNumberCountBeforeAddToCart + 1)

        # cartNumberCountAfterAddToCart = int(navigationBarObj.cart_count_element_text())
        # self.assertNotEqual(cartNumberCountBeforeAddToCart, cartNumberCountAfterAddToCart)

