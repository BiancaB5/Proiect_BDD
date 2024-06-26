from browser import Browser
from pages.login_page import LoginPage
from pages.news_page import WhatsNewPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.wish_list_page import WishListPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()
    context.new_page = WhatsNewPage()
    context.wish_list_page = WishListPage()

def after_all(context):
    context.browser.close()