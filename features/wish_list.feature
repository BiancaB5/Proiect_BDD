Feature: Add to Wish List

  Background: Open home page
    Given I am on the home page

  @wish
  Scenario: Add to Wish List
    When I click LUMA LOGO button
    When I enter "jackets" in the search filed
    And I click the search magnifying button
    And I click Add to Wish List button
    And I click remove button
    Then I am redirected on the wish list results page
