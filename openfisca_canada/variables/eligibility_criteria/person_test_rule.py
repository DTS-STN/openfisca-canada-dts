# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class is_expiring_2021(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"Person has parental consent"