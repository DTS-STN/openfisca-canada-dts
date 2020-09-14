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
        #if persons.family.nb_persons(role=Family.CHILD).any():
        if persons.has_role(Family.PARENT).any():
            return parameters(period).benefitfinder.eligible_periods * (persons('dtc__has_documented_disability', period) +\
                persons.family.any(persons.family.members('dtc__has_documented_disability', period), role=Family.CHILD))
        else:
            return parameters(period).benefitfinder.eligible_periods * persons('dtc__has_documented_disability', period)

class dtc__is_eligible_for_dtc_and_oas(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is person eligible for a disibility tax credit and old age security"

    def formula(persons, period, parameters):
        return parameters(period).benefitfinder.eligible_periods * (persons('dtc__has_documented_disability', period) *\
            persons('oas__is_eligible', period))