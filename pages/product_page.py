from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
        def add_product_to_basket(self):
            self.browser.find_element(*ProductPageLocators.ADD_TO_CARD).click()

        def check_product_name_and_price(self):
            print("'{}' added to cart!".format(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text))
            assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
