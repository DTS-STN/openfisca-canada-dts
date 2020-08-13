# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_canada.entities import Person, Family
import numpy as np


class cerb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb"
    reference = "tbd"

    def formula(persons, period, parameters):
        return (persons('income_status__has_lost_all_income', period) * (persons('income_status_reason__has_lost_job', period) + persons('income_status_reason__has_employer_closed', period) + \
            persons('income_status_reason__has_self_employee_with_no_income', period) + persons('income_status_reason__has_unpaid_leave_to_care_for_child_or_sick', period) + \
            persons('income_status_reason__has_parental_recently_cant_return_to_work', period) + persons('income_status_reason__has_ei_recent_claim_ended', period))) + \
            (persons('income_status__has_lost_some_income', period) * ((persons("income_status_reason__has_hours_reduced",period) + persons("income_status_reason__employed_lost_a_job",period)) * persons("income_status_reason__has_1000_or_less",period))) + \
            (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_quarantined",period)) + \
            (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_self_employed_some_income",period) * persons("income_status_reason__has_1000_or_less",period)) + \
            persons('income_status_reason__is_gross_income_over_5k', period)

class cerb__eligible_scenario(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb"
    reference = "tbd"

    def formula(persons, period, parameters):
        result = np.arange(1)
        if (persons('income_status__has_lost_all_income', period) * (persons('income_status_reason__has_lost_job', period) + persons('income_status_reason__has_employer_closed', period))):
            result[0]=1
        elif (persons('income_status__has_lost_all_income', period) * persons('income_status_reason__has_self_employee_with_no_income', period) + persons('income_status_reason__has_unpaid_leave_to_care_for_child_or_sick', period) + \
            persons('income_status_reason__has_parental_recently_cant_return_to_work', period) + persons('income_status_reason__has_ei_recent_claim_ended', period)):
                result[0]= 4
        elif (persons('income_status__has_lost_some_income', period) * ((persons("income_status_reason__has_hours_reduced",period) + persons("income_status_reason__employed_lost_a_job",period)) * persons("income_status_reason__has_1000_or_less",period))):
                result[0]=  2
        elif (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_quarantined",period)):
                result[0]=  3
        elif  (persons('income_status__has_lost_some_income', period) * persons("income_status_reason__is_self_employed_some_income",period) * persons("income_status_reason__has_1000_or_less",period)):
            result[0]= 5
        elif persons('income_status_reason__is_gross_income_over_5k', period):
            result[0]= 6
        else:
            result[0]=  0
        return result
            