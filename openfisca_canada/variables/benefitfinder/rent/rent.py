# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class rent__is_eligible(Variable):
    value_type = bool
    entity = Person
    default_value = False
    label = u"Is eligible for rent help"
    definition_period = MONTH
    end = "2020-09-30"

    def formula(persons, period, parameters):
        return parameters(period).benefitfinder.eligible_periods * persons("rent__has_need_for_rent_help", period)
    
class rent__has_need_for_rent_help(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"client has need for rent help"

