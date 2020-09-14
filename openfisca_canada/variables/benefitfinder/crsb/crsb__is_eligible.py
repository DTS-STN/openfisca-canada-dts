from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class crsb__is_eligible(Variable):
    value_type = bool
    entity = Person
    label = u"is the claimant eligble for crsb?"
    definition_period = MONTH

    def formula_2020_10(persons, period, parameters):
        return persons("income_status_reason__is_quarantined", period)

