"""SR 824.012.2 Art. 2

Generated from: ch/824/de/824.012.2.md

Hang- und Steillagen: Service days per hectare for slopes of varying steepness.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zdv_wbf_hangflaeche_18_35_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare Hangflaeche mit Neigung 18-35 Prozent"
    reference = "SR 824.012.2 Art. 2 Bst. a"
    default_value = 0.0


class zdv_wbf_hangflaeche_35_50_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare Hangflaeche mit Neigung 35-50 Prozent"
    reference = "SR 824.012.2 Art. 2 Bst. b"
    default_value = 0.0


class zdv_wbf_hangflaeche_ueber_50_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare Hangflaeche mit Neigung ueber 50 Prozent"
    reference = "SR 824.012.2 Art. 2 Bst. c"
    default_value = 0.0


class zdv_wbf_diensttage_hanglagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zustehende Diensttage fuer Hang- und Steillagen"
    reference = "SR 824.012.2 Art. 2"

    def formula(person, period, parameters):
        p = parameters(period).sr_824_012_2

        tage = (
            person('zdv_wbf_hangflaeche_18_35_ha', period) * p.diensttage_hang_18_35 +
            person('zdv_wbf_hangflaeche_35_50_ha', period) * p.diensttage_hang_35_50 +
            person('zdv_wbf_hangflaeche_ueber_50_ha', period) * p.diensttage_hang_ueber_50
        )
        return tage
