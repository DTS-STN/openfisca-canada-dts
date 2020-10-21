from openfisca_core.model_api import *
from openfisca_canada.entities import Person
from openfisca_canada.enums.province import *
from openfisca_canada.enums.common import *

class province_of_residence(Variable):
    value_type = Enum
    possible_values = CanadianProvinceOrTerritory
    default_value = CanadianProvinceOrTerritory.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"Person's province of residence"

class is_canadian(Variable):
    value_type = Enum
    possible_values = BooleanEnum
    default_value = BooleanEnum.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"is person canadian"