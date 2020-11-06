from openfisca_core.model_api import * 
# Import the entities specifically defined for this tax and benefit system 
from openfisca_canada.entities import Person, Family  



class has_medical_certificate(Variable): 
    value_type = bool 
    entity = Person 
    label = u"does this person have a medical certificate?" 
    definition_period = DAY 
    reference = u"TODO"          