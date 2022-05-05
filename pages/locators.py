from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")

class ProductPageLocators():
    ADD_TO_CARD = (By.CSS_SELECTOR,"button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    ALERT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert .alertinner strong')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert .alertinner strong')