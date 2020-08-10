from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person, Family

class is_ei_workshare_eligible(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for the EI Workshare program?"
    definition_period = MONTH
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("has_some_income",period)
        #  + \
        # persons("has_hours_reduced_or_employed_lost_a_job",period) + \
        # persons("has_1000_or_less",period) + \
        # persons("is_self_employed_some_income",period)