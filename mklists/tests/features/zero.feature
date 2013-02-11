Feature: Load configuration file
    In current directory
    Running mklists-dev.py
    The mklists rules should print.

    Scenario: Print Configuration
        Given I have a Rulefile
        When I run mklists-dev.py
        Then I see the configuration variables
