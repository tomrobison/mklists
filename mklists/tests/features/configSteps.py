# -*- coding: utf-8 -*-
import os
from lettuce import *
import mklists_dev


@step(u'Given I have a Rulefile')
def given_i_have_a_rulefile(step):
    rulefilePresent = os.path.isfile('Rulefile')
    assert True == rulefilePresent


@step(u'When I run mklists-dev.py')
def when_i_run_mklists_dev_py(step):
    assert 'success' == mklists_dev.test()


@step(u'Then I see the configuration variables')
def then_i_see_the_configuration_variables(step):
    rules = ['x', 'y', 1, 2]
    assert rules == mklists_dev.main()
