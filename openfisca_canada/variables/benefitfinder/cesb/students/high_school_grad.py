# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class high_school_grad(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is graduating from high school in the year of 2019-2020"

    def formula(persons, period, parameters):
        return persons("no_income_before", period)

