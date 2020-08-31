# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class maternity_benefits__is_eligible_for_maternity_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False

    def formula(persons, period, parameters):
        return persons('maternity_benefits__is_within_qualifying_weeks_to_due_date', period) + \
            persons('maternity_benefits__is_within_qualifying_weeks_after_birth_of_child', period)

class maternity_benefits__weeks_to_due_date(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH

class maternity_benefits__weeks_after_birth_of_child(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH

class maternity_benefits__is_within_qualifying_weeks_to_due_date(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False

    def formula(persons, period, parameters):
        qualifying_weeks_to_due_date = parameters(period).maternity_benefits.maternity_benefits.maternity_benefits__qualifying_weeks_to_due_date
        return persons('maternity_benefits__weeks_to_due_date', period) <= qualifying_weeks_to_due_date

class maternity_benefits__is_within_qualifying_weeks_after_birth_of_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False

    def formula(persons, period, parameters):
        qualifying_weeks_after_birth_of_child = parameters(period).maternity_benefits.maternity_benefits.maternity_benefits__qualifying_weeks_after_birth_of_child
        return persons('maternity_benefits__weeks_after_birth_of_child', period) <= qualifying_weeks_after_birth_of_child

