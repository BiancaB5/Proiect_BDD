Feature: Add to Wish List

  Background: Open home page
    Given I am on the home page

  @wish
  Scenario: Add to Wish List
    When I click LUMA LOGO button
    When I enter "jackets" in the search filed
    And I click the search magnifying button
    And I click Add to Wish List button
    Then I am redirected on the wish list results page


#  @remove
#  Scenario: Remove from Wish List
#    When I click remove button
##    Then Wish list has "1" Item(s) in it
#    Then The URL of the page is "https://magento.softwaretestingboard.com/wishlist/index/index/wishlist_id/136032/"