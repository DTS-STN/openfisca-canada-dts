# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class crcb__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Person is eligible for CRCB benefit"

    #Your childs or dependents school, daycare or care facility closed due to covid-19, you're on unpaid leave to take care for a child or sick person
    def formula(persons, period, parameters):
        return persons("income_status_reason__has_child_or_dependant_with_closed_school_or_daycare_or_facility_due_to_c19", period) + \
        persons("income_status_reason__has_unpaid_leave_to_care_for_child_or_sick", period)
