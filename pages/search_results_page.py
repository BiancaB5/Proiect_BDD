from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import browser
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".action.tocart.primary")
    BUTTON_SIZE = (By.ID, "option-label-size-143-item-167")
    BUTTON_COLOR =(By.ID, 'option-label-color-93-item-50')
    BUTTON_CART =(By.CSS_SELECTOR, '.action.showcart')
    BUTTON_CHECKOUT = (By.ID, 'top-cart-btn-checkout')
    INPUT_STREET_ADDRESS = (By.NAME, 'street[0]')
    INPUT_CITY =(By.NAME, 'city')
    SELECT_STATE = (By.NAME, 'region_id')
    INPUT_POSTAL_CODE =(By.NAME, 'postcode')
    SELECT_COUNTRY =(By.NAME, 'country_id')
    INPUT_PHONE_NUMBER =(By.NAME, 'telephone')
    SHIPPING_METHODS =(By.NAME, 'ko_unique_1')
    BUTTON_NEXT =(By.CLASS_NAME, 'continue')
    CHECK_BILL_BUTTON = (By.CLASS_NAME, "checkout-billing-address")
    BUTTON_PLACE_ORDER = (By.CSS_SELECTOR, '.action.primary.checkout')
    MESSAGE_SUCCESS_ORDER = (By.CLASS_NAME, "page-title")
    BUTTON_REVIEWS = (By.CSS_SELECTOR, ".action.view")
    INPUT_RATING_REV = (By.ID, "Rating_5_label")
    INPUT_NICKNAME = (By.ID, "nickname_field")
    INPUT_SUMMARY = (By.ID, "summary_field")
    INPUT_REVIEW = (By.ID, "review_field")
    BUTTON_SUBMIT_REVIEW = (By.CSS_SELECTOR, ".action.submit")

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
        #asteptam ca butonul sa fie clickuibil
        button_cart = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.BUTTON_CART))
        button_cart.click()

    def click_proceed_checkout(self):
        # asteapta ca elementul cu ID-ul 'cart-items' sa fie localizat pe pagina
        button_checkout = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        button_checkout.click()

    def verify_url_shipping(self, expected_url):
        # afiseaza URL-ul curent
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        # afiseaza URL-ul asteptat
        print("URL-ul asteptat:", expected_url)

        assert self.driver.current_url == expected_url
    def set_street_address(self, text):
        self.type(self.INPUT_STREET_ADDRESS, text)

    def set_city(self, text):
        self.type(self.INPUT_CITY, text)

    def select_state(self, text):
        dropdown = self.find(self.SELECT_STATE)
        Select(dropdown).select_by_visible_text(text)

    def set_postal_code(self, number):
        self.type(self.INPUT_POSTAL_CODE, number)

    def select_country(self, text):
        dropdown = self.find(self.SELECT_COUNTRY)
        Select(dropdown).select_by_visible_text(text)

    def set_phone_number(self, text):
        self.type(self.INPUT_PHONE_NUMBER, text)

    def click_shipping_methods(self):
        self.find(self.SHIPPING_METHODS).click()

    def click_next_button(self):
        self.find(self.BUTTON_NEXT).click()

    def verify_url_payment(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        # afiseaza URL-ul asteptat
        print("URL-ul asteptat:", expected_url)
        assert self.driver.current_url == expected_url

    def click_check_bill_address(self):
        self.find(self.CHECK_BILL_BUTTON).click()
    def click_place_order_button(self):
        self.driver.implicitly_wait(3)
        self.find(self.BUTTON_PLACE_ORDER).click()

    def verify_url_order(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        # afiseaza URL-ul asteptat
        print("URL-ul asteptat:", expected_url)
        assert self.driver.current_url == expected_url
    def verify_success_message_displayed(self):
        self.driver.implicitly_wait(3)
        assert self.find(self.MESSAGE_SUCCESS_ORDER).is_displayed()

    def verify_success_message_contains_text(self, text):
        success_message = self.find(self.MESSAGE_SUCCESS_ORDER).text
        print("Mesajul de succes actual este:", success_message)
        print("Textul asteptat este:", text)
        assert success_message == text

    def verify_error_message_bag(self, text):
        assert text in self.find(self.ERROR_MESSAGE_BAG).text


#SCENARIUL CU REVIEW
    BUTTON_REVIEWS = (By.CSS_SELECTOR, ".action.view")
    INPUT_RATING_REV = (By.CLASS_NAME, "rating-4")
    INPUT_NICKNAME = (By.ID, "nickname_field")
    INPUT_SUMMARY = (By.ID, "summary_field")
    INPUT_REVIEW = (By.ID, "review_field")
    BUTTON_SUBMIT_REVIEW = (By.CSS_SELECTOR, ".action.submit")

    def click_review_button(self):
        self.find(self.BUTTON_REVIEWS).click()

    def click_rating_rev(self):
        # asteapta pana cand elementul devine vizibil
        button_raiting = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.INPUT_RATING_REV))

        # deruleaza in jos pentru a asigura vizibilitatea elementului
        self.driver.execute_script("arguments[0].scrollIntoView();", button_raiting)

        #inlocuieste partea de click() cu actiuni de mouse
        ActionChains(self.driver).move_to_element(button_raiting).click().perform()

    def set_nickname(self, text):
        self.type(self.INPUT_NICKNAME, text)
    def set_summary(self, text):
        self.type(self.INPUT_SUMMARY, text)
    def set_review(self, text):
        self.type(self.INPUT_REVIEW, text)
    def click_submit_review_button(self):
        self.find(self.BUTTON_SUBMIT_REVIEW).click()