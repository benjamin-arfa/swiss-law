"""SR 519.1 Art. 16

Generated from: ch/519/de/519.1.md

Art. 16 Urlaub (Leave):
In addition to BPG/BPV entitlements, personnel have an entitlement to at most
one day of paid leave each before the start and at the end of the deployment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pvspa_zusatzurlaub_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Additional paid leave days for deployment (max 1 before + 1 after = 2)"
    reference = "SR 519.1 Art. 16"

    def formula(person, period, parameters):
        return parameters(period).sr_519_1.zusatzurlaub_tage
