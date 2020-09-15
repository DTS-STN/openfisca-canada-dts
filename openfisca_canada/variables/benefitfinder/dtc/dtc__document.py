# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family

 
class dtc__has_documented_disability(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"has documented disability"
    reference = u"TODO"

class dtc__has_disability(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"has a disability but it is not documented"
    reference = u"TODO"    