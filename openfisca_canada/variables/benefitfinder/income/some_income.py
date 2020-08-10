# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person, Family

class has_lost_some_income(Variable):
    value_type = bool
    entity = Person
    label = u"Does this person have some income?"
    definition_period = MONTH
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("is_quarentined",period) + \
        persons("has_hours_reduced_or_employed_lost_a_job",period) + \
        persons("has_1000_or_less",period) + \
        persons("is_self_employed_some_income",period)

class is_quarentined(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person in quarentine?"
    definition_period = MONTH
    reference = u"TODO"

#We may consider breaking into two variables
class has_hours_reduced_or_employed_lost_a_job(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person working reduced hours or employed lost a job?"
    definition_period = MONTH
    reference = u"TODO"

class has_1000_or_less(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person making #1000 or less?"
    definition_period = MONTH
    reference = u"TODO"

class is_self_employed_some_income(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person self inployed with some income?"
    definition_period = MONTH
    reference = u"TODO"