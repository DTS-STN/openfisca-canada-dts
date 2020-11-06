# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person
from datetime import *

class is_16_or_older(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = DAY
    label = u"Person is 16 years of age and older"

    def formula(persons, period, parameters):
        return (persons("age", period) >= 16) 
        

class age(Variable):
    value_type = int
    entity = Person
    definition_period = DAY
    label = u"Person's date of birth"
    def formula(persons, period, parametes):
        birthdate = persons("date_of_birth", period)
        birth_year = birthdate.astype('datetime64[Y]').astype(int) + 1970
        birth_month = birthdate.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (birthdate - birthdate.astype('datetime64[M]') + 1).astype(int)
        is_birthday_past = (birth_month < period.start.month) + (birth_month == period.start.month) * (birth_day <= period.start.day)
        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)  # If the birthday is not passed this year, substract one year

class date_of_birth(Variable):
    value_type = date
    default_value = date.today()
    entity = Person
    definition_period = ETERNITY # This variable cannot change over time.
    label = u"Person's date of birth"

  