# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *


class reform_ccb(Reform):
    # A reform always defines an `apply` method that builds the reformed tax and benefit system from the reference one.
    # See https://openfisca.org/doc/coding-the-legislation/reforms.html#writing-a-reform
    def apply(self):
        # Our reform neutralizes the `canada_child_benefit__is_eligible` variable. When this reform is applied, `canada_child_benefit__is_eligible` will always return its default value.
        self.neutralize_variable('canada_child_benefit__is_eligible')