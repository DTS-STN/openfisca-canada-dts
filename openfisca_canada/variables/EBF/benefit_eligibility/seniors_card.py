from openfisca_core.model_api import * 
# Import the entities specifically defined for this tax and benefit system 
from openfisca_canada.entities import Person, Family  
from openfisca_canada.variables.common.provinces import *
 

class seniors_card__is_eligible(Variable): 
    value_type = bool 
    entity = Person 
    label = u"Is this person eligible for a seniors card?" 
    definition_period = DAY 
    reference = u"TODO" 
    end = "2021-01-01"   

    def formula(persons, period, parameters):
        person_age = persons("age", period)
        person_province = persons("province_of_residence", period)
        person_is_canadian_resident = persons("is_canadian_resident", period)
        person_is_retired =  persons("is_retired", period)

        return (person_age > 55) *\
            (person_province == CanadianProvinceOrTerritory.ONTARIO) *\
            person_is_canadian_resident *\
            person_is_retired
