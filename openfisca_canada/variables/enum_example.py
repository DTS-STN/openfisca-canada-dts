from openfisca_core.model_api import *
from openfisca_canada.entities import *

# Enumerations are variables that holding a limited set of possible values.
# Openfisca enums are based on Python 3 native enums. Each enum item (for instance: IncomeStatus.all_income) has:
# - a name attribute that contains its key (e.g all_income)
# - a value attribue that contains its description (e.g "lost all income")
class IncomeStatus(Enum):
    ALL_INCOME = "lost all income"
    SOME_INCOME = "lost some income"
    UNCHANGED_INCOME = "lost no income "
    UNKNOWN = "unknown"

class BooleanEnum(Enum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    
class income_status(Variable):
    value_type = Enum
    possible_values = IncomeStatus
    default_value = IncomeStatus.UNKNOWN # The default is mandatory
    entity = Person
    definition_period = MONTH
    label = "the input variable that to be compared with the enum value"


class cerb_is_eligible(Variable):
    value_type = Enum
    possible_values = BooleanEnum
    default_value = BooleanEnum.UNKNOWN
    entity = Person
    definition_period = MONTH
    label = "testing enum scenerio"

    def formula(persons, period, parameters):
        income_status = persons('income_status', period)
        lost_all_income = (income_status == IncomeStatus.ALL_INCOME)
        lost_some_income = (income_status == IncomeStatus.SOME_INCOME)
        lost_no_income = (income_status == IncomeStatus.UNCHANGED_INCOME)
        unknown = (income_status == IncomeStatus.UNKNOWN)

        return (lost_all_income + lost_some_income + lost_no_income + unknown)

        '''if ((lost_all_income + lost_some_income).any()):
            return BooleanEnum.TRUE
        elif (lost_no_income):
            return BooleanEnum.FALSE
        else:
            return BooleanEnum.UNKNOWN'''



