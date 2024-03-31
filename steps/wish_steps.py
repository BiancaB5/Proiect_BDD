from behave import *


@when('I click LUMA LOGO button')
def step_impl(context):
    context.wish_list_page.click_luma_logo()
@when('I click Add to Wish List button')
def step_impl(context):
    context.wish_list_page.click_add_to_wish_list


# @when('I click remove button')
# def step_impl(context):
#     context.wish_list_page.click_remove_wish_item

# @then('Wish list has "{number}" Item(s) in it')
# def step_impl(context, number):
#     context.wish_list_page.verify_wish_list_quantity(number)
@then('I am redirected on the wish list results page')
def step_impl(context):
    context.wish_list_page.verify_url()

# @then("The URL of the page is 'https://magento.softwaretestingboard.com/wishlist/index/index/wishlist_id/136032/'")
# def step_impl(context):
#     context.wish_list_page.verify_url()