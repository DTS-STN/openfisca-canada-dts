# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person
from openfisca_canada.enums.common import *
import datetime

class is_16_and_older(Variable):
    value_type = Enum
    possible_values = BooleanEnum
    default_value = BooleanEnum.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"Person is 16 years of age and older"

    def formula(persons, period, parameters):
        dates_of_birth = (persons("date_of_birth", period))
        is_unknown = (dates_of_birth == DateEnum.UNKNOWN.value)
        is_16 = (dates_of_birth >= period.date)
        is_under_16 = (dates_of_birth < period.date)
        return select(
            [is_unknown, is_16, is_under_16],
            [BooleanEnum.UNKNOWN, BooleanEnum.TRUE, BooleanEnum.FALSE], default=BooleanEnum.UNKNOWN
        )

class date_of_birth(Variable):
    value_type = date
    entity = Person
    definition_period = DAY
    label = u"Person's date of birth"