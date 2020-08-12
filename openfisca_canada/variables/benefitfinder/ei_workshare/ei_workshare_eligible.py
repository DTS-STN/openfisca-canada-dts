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
        return persons("has_some_income_1001_or_more_reduced_hours",period)
   