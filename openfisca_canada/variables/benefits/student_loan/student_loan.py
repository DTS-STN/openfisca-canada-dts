from openfisca_core.model_api import *
from openfisca_canada.entities import Person


class student_loan__is_paying_debt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = false
    label = "Students are given 6 months deferral"
    reference = "to be linked"
