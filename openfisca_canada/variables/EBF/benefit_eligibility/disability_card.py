from openfisca_core.model_api import * 
# Import the entities specifically defined for this tax and benefit system 
from openfisca_canada.entities import Person, Family  
from openfisca_canada.variables.common.provinces import *
 

class disability_card__is_eligible(Variable): 
    value_type = bool 
    entity = Person 
    label = u"Is this person eligible for a disability card?" 
    definition_period = DAY 
    reference = u"TODO" 
    end = "2021-01-01"   

    def formula(persons, period, parameters): 
        return persons("medical_insurance_card__is_eligible", period) *\
        persons("has_medical_certificate", period)

     