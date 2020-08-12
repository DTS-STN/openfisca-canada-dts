# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family

#Disability tax credit
class dtc__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is person eligible for a disibility tax credit"