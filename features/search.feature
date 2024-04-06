Feature: Search

  Background: Open home page
    Given I am on the home page


  Scenario: Search works properly for existing items
    When I enter "bag" in the search filed
    And I click the search magnifying button
    Then I am redirected on the search results page
    And There are some results displayed

  Scenario: Order the item
    When I click the cart button
    And I click the Proceed to Checkout button
    And I am on the Shipping page "https://magento.softwaretestingboard.com/checkout/#shipping"
    And I enter Street Address
    And I enter City
    And I select State
    And I enter Postal Code
    And I select Country
    And I enter Phone Number
    And I choose Shipping Methods
    And I click Next button
    Then I am on the Payment page "https://magento.softwaretestingboard.com/checkout/#payment"