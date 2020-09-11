from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person, Family

class canada_child_benefit__is_eligible(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for the EI Workshare?"
    definition_period = MONTH
    reference = u"TODO"
    def formula_2020_08(persons, period, parameters):
        return parameters(period).benefitfinder.is_eligible__benefits * persons("canada_child_benefit__yes_or_unsure",period)
        #  + \
        # persons("some_income__1001_or_more",period)
    
    def formula_2020_10(persons, period, parameters):
        return parameters(period).benefitfinder.is_eligible__benefits * persons("canada_child_benefit__yes_or_unsure",period)

class canada_child_benefit__yes_or_unsure(Variable):
    value_type = bool
    entity = Person
    label = u"this person is recieving the canada child benefit or is unsure"
    definition_period = MONTH
    reference = u"TODO"

