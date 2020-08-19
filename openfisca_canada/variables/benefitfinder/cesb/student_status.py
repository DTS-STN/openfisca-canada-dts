# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class cesb__is_student_2019_2020(Variable):
    value_type = bool
    entity = Person
    label = u"Is student in the year of 2019-2020"
    definition_period = MONTH

    def formula(persons, period, parameters):
        return persons("cesb__student_lost_job", period) + persons("cesb__has_no_income_before", period)

class cesb__is_high_school_grad(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is graduating from high school in the year of 2019-2020"

    def formula(persons, period, parameters):
        return persons("cesb__has_no_income_before", period)
    
class cesb__student_lost_job(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"student lost job"

class cesb__has_no_income_before(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"student has no income before"