from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def check_if_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
             "Basket item is presented, but should not be"

    def check_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
        "'Your basket is empty.' text is not presented on basket"
