# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class crb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Person is eligible for CRB benefit"

    #def formula(persons, period, parameters):
    #    return true if any of 1,2,3,6,8,9/1b,2b,3b,4b are selected