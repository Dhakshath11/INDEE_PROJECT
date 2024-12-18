#Defined Feature file
Feature: Test Indee Video Player Functionality

  Scenario: Verify user can play, pause, and interact with the video player
    Given I navigate to Indee Tv
    When I sign in using the access code "WVMVHWBS"
    And I navigate to the video section
    And I play the video for 10 seconds
    Then I resume the video
    And I change the volume to 50%
    And I set the resolution to "480p"
    And I pause and exit the player
    And I sign out
