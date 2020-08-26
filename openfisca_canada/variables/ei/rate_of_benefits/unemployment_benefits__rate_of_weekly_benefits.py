# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class unemployment_benefits__rate_of_weekly_benefits(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    default_value = 0.55
    label = 'rate of weekly ensurable earning'

    def formula(persons, period, parameters):
        if (parental_benefits__elected_for_extended_benefits):
            return parameters(period).rate_of_benefits.unemployment_benefits__rate_of_weekly_benefits_parental_extended
        else:
            return parameters(period).rate_of_benefits.unemployment_benefits__rate_of_weekly_benefits

class parental_benefits__elected_for_extended_benefits(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label: 'claimant elects to have parental benefits'