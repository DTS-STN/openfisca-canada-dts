# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person
from datetime import *

class is_16_or_older(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"Person is 16 years of age and older"

    def formula(persons, period, parameters):
        return (persons("age", period) >= 16) 
        

class age(Variable):
    value_type = int
    default_value = date.today()
    entity = Person
    definition_period = MONTH
    label = u"Person's date of birth"
    def formula(persons, period, parametes):
        today = date.today()
        birthdate = persons("date_of_birth", period)[0].astype(datetime)
        return birthdate < today * (today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)))

class date_of_birth(Variable):
    value_type = date
    entity = Person
    definition_period = ETERNITY
    label = u"Person's date of birth"

  