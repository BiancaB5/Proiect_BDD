from behave import *

@given('I am on the Whats New page "{url}"')
def step_impl(context, url):
    context.new_page.open(url)


@then('The new URL of the page is "{url}"')
def step_impl(context, url):
    context.new_page.verify_url(url)