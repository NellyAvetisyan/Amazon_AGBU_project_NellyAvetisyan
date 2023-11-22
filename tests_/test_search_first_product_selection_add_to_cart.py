from pages_.searchResultPage import SearchResultPage
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestwithLoginSteps
from testData_.testData import searchProductName
from pages_.selectedProductDetailPage import SelectedProductDetailPage


class SearchFirstProductSelectionAddToCart(BaseTestwithLoginSteps):
    def test_search_first_product_selection_add_to_cart(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.fill_search_field(searchProductName)
        navigationBarObj.click_to_search_submit_button()

        searchResultPageObj = SearchResultPage(self.simpleDriver)
        searchResultPageObj.click_to_first_product()

        cartCountBeforeAddToCart = navigationBarObj.get_cart_count()

        selectedProductDetailPageObj = SelectedProductDetailPage(self.simpleDriver)
        selectedProductDetailPageObj.click_add_to_cart_button()

        cartCountAfterAddToCart = navigationBarObj.get_cart_count()
        self.assertEqual(cartCountAfterAddToCart, cartCountBeforeAddToCart + 1)





