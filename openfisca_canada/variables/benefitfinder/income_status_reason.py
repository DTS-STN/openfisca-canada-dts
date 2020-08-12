# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family

class income_status_reason__has_lost_job(Variable):
    value_type = bool
    entity = Person
    default_value = False
    definition_period = MONTH
    label = u"has person lost their job"
    reference = ""

class income_status_reason__has_employer_closed(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"has persons employer closed"
    reference = ""

class income_status_reason__has_self_employee_with_no_income(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is self employed person  with no income"
    reference = ""

class income_status_reason__has_unpaid_leave_to_care_for_child_or_sick(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person on unpaid leave to care for child or sick person"
    reference = ""

class income_status_reason__has_parental_recently_cant_return_to_work(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"has person recently returned from parental leave and can't return to work"
    reference = ""

class income_status_reason__has_ei_recent_claim_ended(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"has the persons recent EI claim ended"
    reference = ""

class income_status_reason__is_quarantined(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person in quarantine?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"

#We may consider breaking into two variables
class income_status_reason__has_hours_reduced(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person working reduced hours or employed lost a job?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"

class income_status_reason__employed_lost_a_job(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person working reduced hours or employed lost a job?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"

class income_status_reason__has_1000_or_less(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person making less than 1000?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"

class income_status_reason__has_1001_or_more(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person making less than 1000?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"

class income_status_reason__is_self_employed_some_income(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person self inployed with some income?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"

class income_status_reason__is_gross_income_over_5k(Variable):
    value_type = bool
    entity = Person
    label = u"Is persons gross income over 5000?"
    definition_period = MONTH
    default_value = False
    reference = u"TODO"