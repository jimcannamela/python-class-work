# checkout.feature

Feature: Online store checkout
  Scenario: Applying a discount code
    Given the customer has items in the cart
    When they apply a discount code
    Then the total price should reflect the discount