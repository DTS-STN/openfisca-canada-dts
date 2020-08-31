# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class unemployment_benefits__is_major_attached_claimant(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "claimant is major attached claimant"

    def formula(persons, period, parameters):
        return persons('unemployment_benefits__is_major_attached_claimant', period) + \
            persons('parental_benefits__is_caring_for_one_or_more_new_born_children', period)

class unemployment_benefits__has_more_than_minimum_hours_of_employment_in_qualifying_period(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "Claimant has minimal insurable hours to qualify as a major attached claimant"

class unemployment_benefits__has_more_than_minimum_weeks_of_employment_in_qualifying_period(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "Claimant has minimal insurable weeks to qualify as a major attached claimant"