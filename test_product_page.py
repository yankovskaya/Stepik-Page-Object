import time

import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage


@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name_and_price(link)
    time.sleep(3)   

@pytest.mark.skip   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.skip   
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_product_to_basket()
    page.should_not_be_success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_the_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_if_basket_is_empty()
    basket_page.check_basket_is_empty_text()
