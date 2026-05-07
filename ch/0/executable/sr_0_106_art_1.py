"""SR 0.106 Art. 1

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable
from openfisca_country_groups.entities import Country


class european_committee_for_prevention_of_torture_existance(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "European Committee for Prevention of Torture exists (Art. 1 SR 0.106)"

    def formula(countries, period, parameters):

        return True  # committee exists since article establishes
