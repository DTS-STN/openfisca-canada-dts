# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person, Family

class has_oas(Variable):
    value_type = bool
    default_value = True
    entity = Person
    definition_period = MONTH
    label = u"receiving old age security"

class has_allowance(Variable):
    value_type = bool
    default_value = True
    entity = Person
    definition_period = MONTH
    label = u"receiving allowance"

class has_allowance_for_survivor(Variable):
    value_type = bool
    default_value = True
    entity = Person
    definition_period = MONTH
    label = u"receiving allowance for survivor"