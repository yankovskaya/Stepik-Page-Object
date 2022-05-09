from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
        def add_product_to_basket(self):
            self.browser.find_element(*ProductPageLocators.ADD_TO_CARD).click()

        def get_product_name(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        def get_product_price(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        def check_product_name_and_price(self, link):
            name_in_basket = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_NAME)[0].text
            price_in_basket = self.browser.find_elements(*ProductPageLocators.ALERT_PRICE_IN_BASKET)[2].text
            try:
                assert self.get_product_name() == name_in_basket
                assert self.get_product_price() == price_in_basket
            except AssertionError:
                print(f"{link} ERrror")
            else:
                print("OK")

        def should_not_be_success_message(self):
            assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "FAILED!Success message is presented!"

        def should_not_be_success_message_is_disappeared(self):
            assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "FAILED!Success message is presented!"
