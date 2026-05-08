"""SR 958.2 Art. 4

Generated from: ch/958/fr/958.2.md

Autorisation provisoire de participants étrangers — FINMA may grant provisional
authorization for participation on Swiss trading platforms, valid until the end
of the authorization procedure, max. 1 year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
import numpy as np


class handelsplatz_vorlaeufige_bewilligung(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Foreign participant holds a provisional FINMA authorization for Swiss trading platforms"
    reference = "SR 958.2 Art. 4 al. 1"


class handelsplatz_vorlaeufige_bewilligung_dauer_monate(Variable):
    value_type = int
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Duration in months of the provisional authorization"
    reference = "SR 958.2 Art. 4 al. 1"


class handelsplatz_vorlaeufige_bewilligung_gueltig(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Provisional authorization is still valid (max 12 months)"
    reference = "SR 958.2 Art. 4 al. 1"

    def formula_2019(organisation, period, parameters):
        hat_bewilligung = organisation('handelsplatz_vorlaeufige_bewilligung', period)
        dauer = organisation('handelsplatz_vorlaeufige_bewilligung_dauer_monate', period)

        p = parameters(period).sr958_2
        max_dauer = p.max_vorlaeufige_bewilligung_monate

        return hat_bewilligung * (dauer <= max_dauer)
