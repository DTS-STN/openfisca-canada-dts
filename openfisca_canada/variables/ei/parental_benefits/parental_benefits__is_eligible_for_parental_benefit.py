# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class parental_benefits__is_caring_for_one_or_more_new_born_children(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "claimant caring for one or more new born children"

class parental_benefits__is_caring_for_one_or_more_adopted_children(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "claimant caring for one or more adopted children"

class parental_benefits__is_eligible_for_parental_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "claimant is eligible for parental benefit"

    def formula(persons, period, parameters):
        return persons('unemployment_benefits__is_major_attached_claimant', period) * \
            (persons('parental_benefits__is_caring_for_one_or_more_new_born_children', period) + \
            persons('parental_benefits__is_caring_for_one_or_more_adopted_children', period))
