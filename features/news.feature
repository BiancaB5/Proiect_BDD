Feature: Whats New Page

  Background: Open Whats New page
    Given I am on the Whats New page "https://magento.softwaretestingboard.com/what-is-new.html"

  @newpage
  Scenario: Check that the URL is correct
    Then The new URL of the page is "https://magento.softwaretestingboard.com/what-is-new.html"

#  Scenario: Search new pages info existing
#    When I click the Shop New Yoga button
#    Then I am redirected on the New Luma Yoga Collection page
#    And I should see "New Luma Yoga Collection" Message



