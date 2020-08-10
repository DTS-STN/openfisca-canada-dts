# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family


class cerb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb"
    reference = "tbd"

    def formula(persons, period, parameters):
        return persons('individual_income__has_lost_all_income', period) + \
            persons('individual_income__has_lost_some_income', period) + \
            persons('individual_income__is_gross_income_over_5k', period)
