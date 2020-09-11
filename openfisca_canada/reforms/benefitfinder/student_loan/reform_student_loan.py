# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *


class reform_student_loan(Reform):
    # A reform always defines an `apply` method that builds the reformed tax and benefit system from the reference one.
    # See https://openfisca.org/doc/coding-the-legislation/reforms.html#writing-a-reform
    def apply(self):
        self.neutralize_variable('student_loan__is_eligible')