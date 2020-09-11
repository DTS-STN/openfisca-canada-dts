# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class cesb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"student is eligible for CESB benefit"

    def formula_2020_08(persons, period, parameters):
        return parameters(period).benefitfinder.cesb.cesb__is_eligible * ((persons("cesb__is_student_2019_2020", period) + persons("cesb__is_student_2020_2021", period)) * \
            persons("income_status__has_lost_no_income", period)) + (persons("cesb__is_student_2019_2020", period) * persons("income_status__has_lost_all_income", period))

    def formula_2020_09(persons, period, parameters):
        return parameters(period).benefitfinder.cesb.cesb__is_eligible * (((persons("cesb__is_student_2019_2020", period) + persons("cesb__is_student_2020_2021", period)) * \
            persons("income_status__has_lost_no_income", period)) + (persons("cesb__is_student_2019_2020", period) * persons("income_status__has_lost_all_income", period)))
