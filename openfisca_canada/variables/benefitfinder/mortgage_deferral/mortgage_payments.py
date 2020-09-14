from openfisca_core.model_api import *
from openfisca_canada.entities import Person


class mortgage_deferral__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"Mortgage worries, talk to your bank to get 6 months deferral"
    reference = u"to be linked"

    def formula(persons, period, parameters):
        return parameters(period).benefitfinder.eligible_periods * persons("mortgage_deferral__has_mortgage_payments",period)

class mortgage_deferral__has_mortgage_payments(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"Mortgage worries, person is paying a mortgage"
    reference = u"to be linked"