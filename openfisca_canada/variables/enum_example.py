from openfisca_core.model_api import *
from openfisca_canada.entities import *

# Enumerations are variables that holding a limited set of possible values.
# Openfisca enums are based on Python 3 native enums. Each enum item (for instance: LostAllIncom.lost_job) has:
# - a name attribute that contains its key (e.g lost_job)
# - a value attribue that contains its description (e.g "has lost job")
class LostAllIncome(Enum):
    lost_job = u"has lost job"
    employer_closed = u"has employer closed"
    self_employed = u"is self employed and have no income"
    school_closed = u"has child with closed school"
    unpaid_leave = u"has unpaid leave to care for child or sick"
    quarantined = u"is sick and quarantined"
    parental_leave = u"on parental leave recently, but cannot return to work"
    student = u"is student during 2019-2020 and cannot find work"

class lost_all_income(Variable):
    value_type = Enum
    possible_values = LostAllIncome
    default_value = LostAllIncome.lost_job # The default is mandatory
    entity = Person
    definition_period = MONTH


