Feature: Search

  Background: Open home page
    Given I am on the home page

  @login
  Scenario: New Review for existing items
    When I enter "bag" in the search filed
    And I click the search magnifying button
    And I am redirected on the search results page
    And There are some results displayed
    And I click Reviews button
    And I click 5 stars Raiting
    And I write the Nickname "Anna"
    And I write the summary "Good product"
    And I write the Review "I order the black bag and i like the material, quality product"
    Then I click on the Submit Review button


  Scenario: Order the item
    When I click the cart button
    And I click the Proceed to Checkout button
    And I am on the Shipping page "https://magento.softwaretestingboard.com/checkout/#shipping"
    And I enter Street Address
    And I enter City
    And I select State "Arizona"
    And I enter Postal Code "12345"
    And I select Country "United States"
    And I enter Phone Number
    And I choose Shipping Methods
    And I click Next button
    And I check the confirmation for bill address
    And I click Place Order button
    Then I am redirected on the success order page "https://magento.softwaretestingboard.com/checkout/#payment"
    And Success order message is displayed
    And The success order message is "Checkout"
