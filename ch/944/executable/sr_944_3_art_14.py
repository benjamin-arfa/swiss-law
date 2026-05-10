"""SR 944.3 Art. 14-16

Generated from: ch/944/de/944.3.md

Haftung bei Pauschalreisen: Liability of organiser/intermediary.
Liability for personal injury cannot be limited. For other damages,
liability can be limited to 2x the package price (except for
intentional or grossly negligent damage).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pauschalreise_ist_personenschaden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Personenschaden vorliegt"
    reference = "SR 944.3 Art. 16 Abs. 1"
    default_value = False


class pauschalreise_ist_vorsatz_oder_grobfahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Schaden absichtlich oder grobfahrlaessig zugefuegt wurde"
    reference = "SR 944.3 Art. 16 Abs. 2"
    default_value = False


class pauschalreise_schaden_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Schadenbetrag (CHF)"
    reference = "SR 944.3 Art. 14"
    default_value = 0.0


class pauschalreise_haftung_beschraenkbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Haftung vertraglich beschraenkt werden kann"
    reference = "SR 944.3 Art. 16"

    def formula(person, period, parameters):
        import numpy as np
        personenschaden = person('pauschalreise_ist_personenschaden', period)
        vorsatz = person('pauschalreise_ist_vorsatz_oder_grobfahrlaessig', period)
        # Personenschaden: nie beschraenkbar; Vorsatz/Grobfahrlaessigkeit: nie beschraenkbar
        return np.logical_not(np.maximum(personenschaden, vorsatz))


class pauschalreise_haftungsgrenze(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale vertragliche Haftungsbeschraenkung (CHF)"
    reference = "SR 944.3 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        preis = person('pauschalreise_preis_original', period)
        beschraenkbar = person('pauschalreise_haftung_beschraenkbar', period)
        schaden = person('pauschalreise_schaden_betrag', period)

        # Haftung kann auf 2x Pauschalreisepreis beschraenkt werden
        grenze = preis * 2
        return np.where(beschraenkbar, grenze, schaden)
