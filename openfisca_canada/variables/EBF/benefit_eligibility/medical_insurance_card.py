from openfisca_core.model_api import * 
# Import the entities specifically defined for this tax and benefit system 
from openfisca_canada.entities import Person, Family 
from openfisca_canada.variables.common.provinces import *

class medical_insurance_card__is_eligible(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for a medical insurance card?"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("is_canadian_citizen",period) * \
        persons("has_permanent_address",period) * \
        persons("is_canadian_resident",period)

