from openfisca_core.model_api import *
from openfisca_canada.entities import Person


class student_loan__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"Students is eligible for a 6 months deferral"
    reference = u"to be linked"
    end = "2020-09-30"

    def formula(persons, period, parameters):
        return persons("student_loan__has_student_debt",period)

class student_loan__has_student_debt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"Person is paying an student loan"
    reference = u"to be linked"
