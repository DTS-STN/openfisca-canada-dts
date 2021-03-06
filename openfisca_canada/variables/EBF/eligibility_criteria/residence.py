
from openfisca_core.model_api import *
from openfisca_canada.entities import Person
from openfisca_canada.variables.common.provinces import *

class province_of_residence(Variable):
    value_type = Enum
    possible_values = CanadianProvinceOrTerritory
    default_value = CanadianProvinceOrTerritory.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"Person's province of residence"

class is_resident_of_ontario(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = DAY
    label = u"Person is a resident of Ontario"
    
    def formula(persons, period, parameters):
        person_province = persons("province_of_residence", period)
        return ( person_province == CanadianProvinceOrTerritory.ONTARIO)

class is_canadian_resident(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = DAY
    label = u"is person canadian resident"

class is_canadian_citizen(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = DAY
    label = u"is person canadian citizen"

class has_permanent_address(Variable): 
    value_type = bool
    default_value = False 
    entity = Person 
    label = u"does this person have a permanent address" 
    definition_period = DAY 
    reference = u"TODO"         