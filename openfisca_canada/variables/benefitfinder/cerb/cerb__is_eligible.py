# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family


class cerb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb"
    reference = "tbd"

    def formula(persons, period, parameters):
        return (persons('income_status__has_lost_all_income', period) * (persons('income_status_reason__has_lost_job', period) + persons('income_status_reason__has_employer_closed', period) + \
            persons('income_status_reason__has_self_employee_with_no_income', period) + persons('income_status_reason__unpaid_leave_to_care_for_child_or_sick', period) + \
            persons('income_status_reason__has_parental_recently_cant_return_to_work', period) + persons('income_status_reason__has_ei_recent_claim_ended', period))) + \
            (persons('income_status__has_lost_some_income', period) * ((persons("income_status_reason__has_hours_reduced",period) + persons("income_status_reason__employed_lost_a_job",period)) * persons("income_status_reason__has_1000_or_less",period))) + \
            (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_quarantined",period)) + \
            (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_self_employed_some_income",period) * persons("income_status_reason__has_1000_or_less",period)) + \
            persons('income_status_reason__is_gross_income_over_5k', period)

class cerb__eligible_scenario_number(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb"
    reference = "tbd"

    def formula(persons, period, parameters):
        if (persons('income_status__has_lost_all_income', period) * (persons('income_status_reason__has_lost_job', period) + persons('income_status_reason__has_employer_closed', period))):
            return 1
        if (persons('income_status__has_lost_all_income', period) * persons('income_status_reason__has_self_employee_with_no_income', period) + persons('income_status_reason__unpaid_leave_to_care_for_child_or_sick', period) + \
            persons('income_status_reason__has_parental_recently_cant_return_to_work', period) + persons('income_status_reason__has_ei_recent_claim_ended', period)):
                return 4
        if (persons('income_status__has_lost_some_income', period) * ((persons("income_status_reason__has_hours_reduced",period) + persons("income_status_reason__employed_lost_a_job",period)) * persons("income_status_reason__has_1000_or_less",period))):
                return 2
        if (persons('income_status_has_lost_some_income', period) * persons("income_status_reason__is_quarantined",period)):
                return 3
        if  (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_self_employed_some_income",period) * persons("income_status_reason__has_1000_or_less",period)):
            return 5
        if persons('income_status_reason__is_gross_income_over_5k', period):
            return 6
        else:
            return 0
            