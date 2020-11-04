# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class has_parental_consent(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = DAY
    label = u"Person has parental consent"