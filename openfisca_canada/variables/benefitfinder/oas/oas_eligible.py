# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person, Family

class oas__is_eligible(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"oas is eligible"

    def formula(persons, period, parameters):
        return persons("has_oas", period) + persons("has_allowance", period) + persons("has_allowance_for_survivor", period)