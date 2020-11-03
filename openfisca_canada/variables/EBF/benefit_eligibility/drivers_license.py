
from openfisca_core.model_api import *
from openfisca_canada.entities import Person
from openfisca_canada.variables.common.provinces import *


class drivers_license__is_eligible(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"Person is eligible for a drivers license"
    
    def formula(persons, period, parameters):
        person_province = persons("province_of_residence", period)
        person_16_or_older = persons("is_16_or_older", period)
        person_is_canadian_resident = persons("is_canadian_resident",period)
        person_has_completed_driver_course = persons("has_completed_driver_training", period)
        person_has_parental_consent = persons("has_parental_consent",period)
        person_is_expiring_2021 = persons("is_expiring_2021",period)
        
        return ( person_province != CanadianProvinceOrTerritory.UNKNOWN) *\
            person_16_or_older * person_is_canadian_resident * person_has_completed_driver_course *\
            person_has_parental_consent * person_is_expiring_2021