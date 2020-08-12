# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class is_student_2019_2020(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Is student in the year of 2019-2020"
    definition_period = MONTH

    def formula(persons, period, parameters):
        return persons("student_lost_job", period) + persons("has_no_income_before", period)

class is_high_school_grad(Variable):
    value_type = bool
    default_value = True
    entity = Person
    definition_period = MONTH
    label = u"Is graduating from high school in the year of 2019-2020"

    def formula(persons, period, parameters):
        return persons("has_no_income_before", period)
    
class student_lost_job(Variable):
    value_type = bool
    default_value = True
    entity = Person
    definition_period = MONTH
    label = u"student lost job"

class has_no_income_before(Variable):
    value_type = bool
    default_value = True
    entity = Person
    definition_period = MONTH
    label = u"student has no income before"