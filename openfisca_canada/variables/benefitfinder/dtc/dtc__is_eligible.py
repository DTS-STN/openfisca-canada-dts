# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family

#Disability tax credit
class dtc__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is person eligible for a disibility tax credit"

    def formula(persons, period, parameters):
        return persons('dtc__is_yourself', period) +\
            persons('dtc__is_your_child', period)

class dtc__is_eligible_for_dts_and_oas(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is person eligible for a disibility tax credit and old age security"

    #return persons('dtc__is_yourself', period) * return persons('oas_is_eligible', period)
    def formula(persons, period, parameters):
        return persons('dtc__is_yourself', period)