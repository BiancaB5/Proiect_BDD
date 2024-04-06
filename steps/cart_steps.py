from behave import *

@when('I click size button')
def step_impl(context):
    context.search_results_page.click_size()

@when('I click color button')
def step_impl(context):
    context.search_results_page.click_color()

@when('I click Add to cart button')
def step_impl(context):
    context.search_results_page.click_add_to_cart()

@then('Cart has "{number}" item in it')
def step_impl(context, number):
    context.search_results_page.verify_cart_quantity(number)


# #de aici incepe comanda
#
# @when('I click the cart button')
# def step_impl(context):
#     context.search_results_page.click_cart()
#
# @when('I click the Proceed to Checkout button')
# def step_impl(context):
#     context.search_results_page.click_proceed_checkout()
#
# @when('I am on the Shipping page "https://magento.softwaretestingboard.com/checkout/#shipping"')
# def step_impl(context):
#     context.search_results_page.verify_url_shipping()
#
# @when('I enter Street Address')
# def step_impl(context):
#     context.search_results_page.set_street_address('Magheranului')
#
# @when('I enter City')
# def step_impl(context):
#     context.search_results_page.set_city('Sibiu')
#
# @when('I select State')
# def step_impl(context, text):
#     context.search_results_page.select_state(text)
#
# @when('I enter Postal Code')
# def step_impl(context):
#     context.search_results_page.set_postal_code('123457')
#
# @when('I select Country')
# def step_impl(context, text):
#     context.search_results_page.select_country(text)
#
# @when('I enter Phone Number')
# def step_impl(context):
#     context.search_results_page.set_phone_number('0746823958')
#
# @when('I choose Shipping Methods')
# def step_impl(context):
#     context.search_results_page.click_shipping_methods()
#
# @when('I click Next button')
# def step_impl(context):
#     context.search_results_page.click_next_button()
#
# @then('I am on the Payment page "https://magento.softwaretestingboard.com/checkout/#payment"')
# def step_impl(context):
#     context.search_results_page.verify_url_payment()
















