from behave import *

@given('I am on the home page')
def step_impl(context):
    context.home_page.open()

@when('I enter "{text}" in the search filed')
def step_impl(context, text):
    context.home_page.set_search_term(text)

@when('I click the search magnifying button')
def step_impl(context):
    context.home_page.click_search_magnifying_button()

@then('I am redirected on the search results page')
def step_impl(context):
    context.search_results_page.verify_url()

@then('There are some results displayed')
def step_impl(context):
    context.search_results_page.verify_search_results_displayed()

##de aici
@when('I click the cart button')
def step_impl(context):
    context.search_results_page.click_cart()

@when('I click the Proceed to Checkout button')
def step_impl(context):
    context.search_results_page.click_proceed_checkout()

@when('I am on the Shipping page "{url}"')
def step_impl(context, url):
    context.search_results_page.verify_url_shipping(url)

@when('I enter Street Address')
def step_impl(context):
    context.search_results_page.set_street_address('Magheranului')

@when('I enter City')
def step_impl(context):
    context.search_results_page.set_city('Sibiu')

@when('I select State')
def step_impl(context, text):
    context.search_results_page.select_state(text)

@when('I enter Postal Code')
def step_impl(context):
    context.search_results_page.set_postal_code('123457')

@when('I select Country')
def step_impl(context, text):
    context.search_results_page.select_country(text)

@when('I enter Phone Number')
def step_impl(context):
    context.search_results_page.set_phone_number('0746823958')

@when('I choose Shipping Methods')
def step_impl(context):
    context.search_results_page.click_shipping_methods()

@when('I click Next button')
def step_impl(context):
    context.search_results_page.click_next_button()

@then('I am on the Payment page "{url}"')
def step_impl(context, url):
    context.search_results_page.verify_url_payment(url)