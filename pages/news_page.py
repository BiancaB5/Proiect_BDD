from pages.base_page import BasePage


class WhatsNewPage(BasePage):

#definim locatorii cu litere mari pentru ca sunt constante, nu isi schimba niciodata valoarea
    WHATS_NEW_PAGE_URL = "https://magento.softwaretestingboard.com/what-is-new.html"


    def open(self):
        self.driver.get(self.WHATS_NEW_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.WHATS_NEW_PAGE_URL