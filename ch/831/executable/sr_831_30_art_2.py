"""SR 831.30 Art. 2

Generated from: ch/831/de/831.30.md

Art. 2: Grundsatz - Principle of supplementary benefits.

Abs. 1: The Confederation and cantons grant supplementary benefits (EL)
to persons meeting the conditions of Art. 4-6, to cover their
subsistence needs.

Abs. 2: Cantons may provide benefits beyond this law and set special
conditions. Employer contributions are excluded.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_voraussetzungen_art4_bis_6_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person erfuellt die Voraussetzungen nach Art. 4-6 ELG"
    reference = "SR 831.30 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        grundanspruch = person('el_grundanspruch', period)
        vermoegen_ok = person('el_vermoegen_unter_schwelle', period.this_year)
        return grundanspruch * vermoegen_ok


class el_anspruch_grundsatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Grundsaetzlicher Anspruch auf Ergaenzungsleistungen (Art. 2 ELG)"
    reference = "SR 831.30 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return person('el_voraussetzungen_art4_bis_6_erfuellt', period)
