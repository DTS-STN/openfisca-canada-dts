# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class student_financial_help__is_eligible(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"student financial help eligibility"

    def formula(persons, period, parameters):
        return parameters(period).benefitfinder.eligible_periods * persons("student_financial_help__has_plan_for_school", period)

class student_financial_help__has_plan_for_school(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"student plans to go to school"