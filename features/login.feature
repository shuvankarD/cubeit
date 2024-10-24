Feature: Login

Scenario: Successful Login
    Given username and pwd password
    When Log In button clicked
    Then show welcome message
    