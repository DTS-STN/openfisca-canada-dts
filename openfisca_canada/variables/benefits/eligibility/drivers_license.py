from openfisca_core.model_api import *
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

        persons_16_and_older = persons("is_16_and_older", period)
        persons_residence = persons("province_of_residence", period)
        has_completed_driver_course = persons("has_completed_driver_course", period)
        has_parental_consent_for_driving_license = persons("has_parental_consent_for_driving_license", period)

        is_unknown = (persons_16_and_older == BooleanEnum.UNKNOWN) +\
            (persons_residence == CanadianProvinceOrTerritory.UNKNOWN) +\
            (has_completed_driver_course == BooleanEnum.UNKNOWN) +\
            (has_parental_consent_for_driving_license == BooleanEnum.UNKNOWN)

        is_true = (persons_16_and_older == BooleanEnum.TRUE) *\
            (persons_residence == CanadianProvinceOrTerritory.ONTARIO) *\
            (has_completed_driver_course == BooleanEnum.TRUE) *\
            (has_parental_consent_for_driving_license == BooleanEnum.TRUE)

        is_false = (persons_16_and_older == BooleanEnum.FALSE) +\
            ((persons_residence != CanadianProvinceOrTerritory.ONTARIO) + (persons_residence != CanadianProvinceOrTerritory.UNKNOWN)) +\
            (has_completed_driver_course == BooleanEnum.FALSE) +\
            (has_parental_consent_for_driving_license == BooleanEnum.FALSE)
            
        return select(
            [is_unknown, is_true, is_false],
            [BooleanEnum.UNKNOWN, BooleanEnum.TRUE, BooleanEnum.FALSE], default=BooleanEnum.UNKNOWN
        )

class has_completed_driver_course(Variable):
    value_type = Enum
    possible_values = BooleanEnum
    default_value = BooleanEnum.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"Person has completed driver course"

class has_parental_consent_for_driving_license(Variable):
    value_type = Enum
    possible_values = BooleanEnum
    default_value = BooleanEnum.UNKNOWN
    entity = Person
    definition_period = DAY
    label = u"Person has consent for driving license"