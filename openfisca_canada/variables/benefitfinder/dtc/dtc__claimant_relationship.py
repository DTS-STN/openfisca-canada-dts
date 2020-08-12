# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family


class dtc__is_yourself(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is person applying for themself"

class dtc__is_your_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is person applying for their child"
