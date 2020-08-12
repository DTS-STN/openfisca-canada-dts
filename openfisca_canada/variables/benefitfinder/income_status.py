# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family


class income_status__has_lost_all_income(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"has person lost all income"
    reference = "tbd"

class income_status__has_lost_some_income(Variable):
    value_type = bool
    entity = Person
    label = u"has this person lost some income?"
    definition_period = MONTH
    reference = u"TODO"

class income_status__has_lost_no_income(Variable):
    value_type = bool
    entity = Person
    label = u"has this person lost no income?"
    definition_period = MONTH
    reference = u"TODO"   
    
