from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

#definim locatorii cu litere mari pentru ca sunt constante, nu isi schimba niciodata valoarea

    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_SIGNIN = (By.ID, "send2")
    DIV_ERROR_MESSAGE = (By.CLASS_NAME, "message-error")
    BUTTON_CONSENT = (By.CLASS_NAME, "fc-button-label")
    def open(self, url):
        self.driver.get(url)

#drepturi de date
    def click_consent_button(self):
        self.find(self.BUTTON_CONSENT).click()

#verifica url-ul paginii
    def verify_url(self, url):
        assert self.driver.current_url == url


#metoda care scrie pe inputul de email
    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_signin_button(self):
        self.find(self.BUTTON_SIGNIN).click()

    # def verify_account_signin_was_incorrect_message(self):
    #     assert "The account sign-in was incorrect or your account is disabled temporarily." in self.find(self.DIV_ERROR_MESSAGE).text

#sau varianta de metoda mai generalizata pentru mesajul de eroare
    def verify_signin_error_message(self, text):
        assert text in self.find(self.DIV_ERROR_MESSAGE).text