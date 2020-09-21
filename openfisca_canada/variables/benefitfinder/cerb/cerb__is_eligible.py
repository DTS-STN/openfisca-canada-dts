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
    end = "2020-09-26"

    def formula_2020_03(persons, period, parameters):
        return persons('cerb__is_eligible_lost_all_income_lost_job_or_employer_closed', period) +\
                persons('cerb__is_eligible_lost_some_income_reduced_hours_1000_or_less', period) +\
                persons('cerb__is_eligible_lost_some_income_quarantine', period) +\
                persons('cerb__is_eligible_lost_all_income_self_employed_closed_unpaid_leave_parental_leave_recent_ei_claim', period) +\
                persons('cerb__is_eligible_lost_some_income_self_employed_1000_hours_or_less', period) +\
                persons('cerb__is_eligible_gross_income_over_5k', period) +\
                persons('cerb__is_eligible_lost_all_income_lost_job_and_no_income_quarantine', period)

    def formula_2020_09(persons, period, parameters):
        return (persons('has_not_received_cerb', period) == False) *\
                (persons('cerb__have_exhausted', period) == False) +\
                ((persons('has_not_received_cerb', period) == True) *\
                persons('cerb__is_eligible_lost_all_income_lost_job_or_employer_closed', period) +\
                persons('cerb__is_eligible_lost_some_income_reduced_hours_1000_or_less', period) +\
                persons('cerb__is_eligible_lost_some_income_quarantine', period) +\
                persons('cerb__is_eligible_lost_all_income_self_employed_closed_unpaid_leave_parental_leave_recent_ei_claim', period) +\
                persons('cerb__is_eligible_lost_some_income_self_employed_1000_hours_or_less', period) +\
                persons('cerb__is_eligible_gross_income_over_5k', period) +\
                persons('cerb__is_eligible_lost_all_income_lost_job_and_no_income_quarantine', period))
   
class has_not_received_cerb(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"have claimant received cerb before?"

class cerb__have_exhausted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"cerb exhausted"

class cerb__payment_almost_up(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"cerb almost up"
        
class cerb__is_eligible_lost_all_income_lost_job_or_employer_closed(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"which scenario of cerb is person eligible?"
    reference = "tbd"

    def formula(persons, period, parameters):
        return persons('income_status__has_lost_all_income', period) * (persons('income_status_reason__has_lost_job', period) +\
            persons('income_status_reason__has_employer_closed', period))

class cerb__is_eligible_lost_all_income_lost_job_and_no_income_quarantine(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"is person eligible for cerb?"
    reference = "tbd"

    def formula(persons, period, parameters):
        return persons('income_status__has_lost_all_income', period) * persons('income_status_reason__is_quarantined', period)

class cerb__is_eligible_lost_some_income_reduced_hours_1000_or_less(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"which scenario of cerb is person eligible?"
    reference = "tbd"
    
    def formula(persons, period, parameters):
        return persons('income_status__has_lost_some_income', period) * ((persons('income_status_reason__has_hours_reduced', period) + \
            persons('income_status_reason__employed_lost_a_job', period)) * persons('income_status_reason__has_1000_or_less', period))

class cerb__is_eligible_lost_some_income_quarantine(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"which scenario of cerb is person eligible?"
    reference = "tbd"
    
    def formula(persons, period, parameters):
        return persons('income_status__has_lost_some_income', period) * persons('income_status_reason__is_quarantined', period)
            


class cerb__is_eligible_lost_all_income_self_employed_closed_unpaid_leave_parental_leave_recent_ei_claim(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb__is_eligible_lost_all_income_self_employed_closed_unpaid_leave_parental_leave_recent_ei_claim?"
    reference = "tbd"
    
    def formula(persons, period, parameters):
        return persons('income_status__has_lost_all_income', period) * (persons('income_status_reason__is_self_employed', period) + \
            persons('income_status_reason__has_unpaid_leave_to_care_for_child_or_sick', period) + \
            persons('income_status_reason__has_parental_recently_cant_return_to_work', period) + \
            persons('income_status_reason__has_ei_recent_claim_ended', period))

class cerb__is_eligible_lost_some_income_self_employed_1000_hours_or_less(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible for cerb__is_eligible_lost_some_income_self_employed_1000_hours_or_less?"
    reference = "tbd"
    
    def formula(persons, period, parameters):
        return persons('income_status__has_lost_some_income', period) * persons('income_status_reason__is_self_employed', period) * \
            persons('income_status_reason__has_1000_or_less', period)

class cerb__is_eligible_gross_income_over_5k(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = u"is person eligible fo cerb__is_eligible_gross_income_over_5k?"
    reference = "tbd"
    
    def formula(persons, period, parameters):
        return persons('income_status_reason__is_gross_income_over_5k', period)