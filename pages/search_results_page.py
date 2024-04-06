from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".action.tocart.primary")
    BUTTON_SIZE = (By.ID, "option-label-size-143-item-167")
    BUTTON_COLOR =(By.ID, 'option-label-color-93-item-50')

    BUTTON_CART =(By.CLASS_NAME, 'showcart')
    BUTTON_CHECKOUT = (By.ID, 'top-cart-btn-checkout')
    INPUT_STREET_ADDRESS = (By.ID, 'LHT7CWU')
    INPUT_CITY =(By.ID, 'VQII9DR')
    SELECT_STATE =(By.ID, 'XE5BJYP')
    INPUT_POSTAL_CODE =(By.ID, 'IM35MRM')
    SELECT_COUNTRY =(By.ID, 'DM3V04Q')
    INPUT_PHONE_NUMBER =(By.ID, 'YYEHUWT')
    SHIPPING_METHODS =(By.NAME, 'ko_unique_1')
    BUTTON_NEXT =(By.CLASS_NAME, 'continue')
    BUTTON_PLACE_ORDER =(By.CLASS_NAME, 'checkout')
    # URL_SHIPPING = "https://magento.softwaretestingboard.com/checkout/#shipping"
    URL_PAYMENT = "https://magento.softwaretestingboard.com/checkout/#payment"

    def verify_url(self):
        assert "https://magento.softwaretestingboard.com/catalogsearch/result/?q=bag" in self.driver.current_url

    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0

    def click_size(self):
        self.find(self.BUTTON_SIZE).click()
    def click_color(self):
        self.find(self.BUTTON_COLOR).click()
    def click_add_to_cart(self):
        self.driver.implicitly_wait(3)
        self.find(self.BUTTON_ADD_TO_CART).click()

    def click_cart(self):
        self.driver.implicitly_wait(3)
        self.find(self.BUTTON_CART).click()

    def click_proceed_checkout(self):
        self.driver.implicitly_wait(3)
        self.find(self.BUTTON_CHECKOUT).click()

    def verify_url_shipping(self):
        self.driver.implicitly_wait(3)
        assert self.driver.current_url == url

    def set_street_address(self, text):
        self.type(self.INPUT_STREET_ADDRESS, text)

    def set_city(self, text):
        self.type(self.INPUT_CITY, text)

    def select_state(self, text):
        self.select_dropdown_text(self.SELECT_STATE, text)

    def set_postal_code(self, text):
        self.type(self.INPUT_POSTAL_CODE, text)

    def select_country(self, text):
        self.select_dropdown_text(self.SELECT_COUNTRY, text)

    def set_phone_number(self, text):
        self.type(self.INPUT_PHONE_NUMBER, text)

    def click_shipping_methods(self):
        self.find(self.SHIPPING_METHODS).click()

    def click_next_button(self):
        self.find(self.BUTTON_NEXT).click()

    def verify_url_payment(self):
        assert self.driver.current_url == self.URL_PAYMENT



