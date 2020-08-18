# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class cesb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"student is eligible for CESB benefit"

    def formula_2020_08(persons, period, parameters):
        return parameters(period).cesb__is_eligible * (persons("is_student_2019_2020", period) + persons("is_high_school_grad", period))

    def formula_2020_09(persons, period, parameters):
        return parameters(period).cesb__is_eligible * (persons("is_student_2019_2020", period) + persons("is_high_school_grad", period))
