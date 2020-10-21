# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person
from openfisca_canada.enums.common import *
from openfisca_canada.enums.province import *

class drivers_license__is_eligible(Variable):
    value_type = Enum
    possible_values = BooleanEnum
    default_value = BooleanEnum.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"Person is eligible for a drivers license"

    def formula(persons, period, parameters):
        persons_16_and_older = (persons("is_16_and_older", period))
        persons_residence = persons("province_of_residence", period)
        ontario_residence = (persons_residence == Province.ONTARIO)
        return persons_16_and_older == ontario_residence