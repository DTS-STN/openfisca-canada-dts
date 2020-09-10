# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class crb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Person is eligible for CRB benefit"

    #lost your job, your employer closed, You are self emplyoed and have no income, you are sick in mandatory quarantine and on unpaid leave,You were in collage 2019-2020 and cant find work, you were on ei reg or fish ended after dec 29 2019
    #Reduced hours due to covid, lost one or two part time jobs, self employed and lost some income but still have some paid work, retired and lost part time work
    def formula(persons, period, parameters):
        return persons("income_status_reason__has_lost_job", period) + \
        persons("income_status_reason__has_employer_closed", period) + \
        persons("income_status_reason__is_self_employed", period) + \
        persons("income_status_reason__is_quarantined", period) + \
        persons("is_college_or_university_student_during_2019_2020_year_and_cannot_find_work", period) + \
        persons("income_status_reason__has_ei_recent_claim_ended", period) + \
        persons("income_status_reason__has_hours_reduced", period) + \
        persons("income_status_reason__employed_lost_a_job", period) + \
        persons("income_status_reason__is_self_employed_with_some_income", period) + \
        persons("income_status_reason__is_retired_and_lost_part_time_work", period)
