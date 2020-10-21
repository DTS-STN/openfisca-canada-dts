# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class drivers_license__is_eligible(Variable):
    value_type = Enum
    entity = Person
    definition_period = MONTH
    label = u"Person is eligible for a drivers license"