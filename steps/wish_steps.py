from behave import *


@when('I click LUMA LOGO button')
def step_impl(context):
    context.wish_list_page.click_luma_logo()

@when('I click Add to Wish List button')
def step_impl(context):
    context.wish_list_page.click_add_to_wish_list

@when('I click remove button')
def step_impl(context):
    context.wish_list_page.click_remove_wish_item

@then('I am redirected on the wish list results page')
def step_impl(context):
    context.wish_list_page.verify_url()
