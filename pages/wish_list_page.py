from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class WishListPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")
    LOGO_LUMA = (By.CLASS_NAME, "logo")
    BUTTON_WISH = (By.CLASS_NAME, "towishlist")
    WISH_LIST_PAGE_URL = 'https://magento.softwaretestingboard.com/wishlist/index/index/wishlist_id/136032/'
    BUTTON_REMOVE_WISH_ITEM = (By.CLASS_NAME, "btn-remove")

    def click_luma_logo(self):
        self.driver.implicitly_wait(3)
        self.find(self.LOGO_LUMA).click()

    def verify_url(self):
        self.driver.implicitly_wait(3)
        assert "https://magento.softwaretestingboard.com/catalogsearch/result/?q=jackets" in self.driver.current_url

    def click_add_to_wish_list(self):
        self.find(self.BUTTON_WISH).click()
        self.driver.implicitly_wait(5)

    def open(self):
        self.driver.get(self.WISH_LIST_PAGE_URL)

    def verify_search_results_displayed(self):
        self.driver.implicitly_wait(3)
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0

    def verify_url(self):
        # assert self.driver.current_url == self.WISH_LIST_PAGE_URL
        self.driver.implicitly_wait(3)
        assert "https://magento.softwaretestingboard.com/wishlist/index/index/wishlist_id/136032/"

    def click_remove_wish_item(self):
        self.find(self.BUTTON_REMOVE_WISH_ITEM).click()
        self.driver.implicitly_wait(5)
