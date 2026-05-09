"""SR 741.01 Art. 15e - Sperrfrist nach Fahren ohne Ausweis

Generated from: ch/de/741/741.01.md

Ban period after driving without license:
- Abs. 1: min 6 months (no license at all)
- Abs. 2: 2 years if also Art. 16c Abs. 2 abis fulfilled
         10 years on repeat
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class fahren_ohne_ausweis_begangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Motorfahrzeug ohne Fuehrerausweis gefuehrt wurde"
    reference = "SR 741.01 Art. 15e Abs. 1"


class zusaetzlich_art16c_abs2_abis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob zusaetzlich Art. 16c Abs. 2 Bst. abis (Raserdelikt) erfuellt ist"
    reference = "SR 741.01 Art. 15e Abs. 2"


class wiederholungsfall_art15e(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Wiederholungsfall nach Art. 15e Abs. 2 vorliegt"
    reference = "SR 741.01 Art. 15e Abs. 2"


class sperrfrist_art15e_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Sperrfrist nach Art. 15e in Monaten"
    reference = "SR 741.01 Art. 15e"

    def formula(person, period, parameters):
        ohne_ausweis = person('fahren_ohne_ausweis_begangen', period)
        art16c_abis = person('zusaetzlich_art16c_abs2_abis', period)
        wiederholung = person('wiederholungsfall_art15e', period)
        # Abs. 2 repeat: 10 years = 120 months
        # Abs. 2 first: 2 years = 24 months
        # Abs. 1 basic: 6 months
        return ohne_ausweis * (
            where(art16c_abis * wiederholung, 120,
            where(art16c_abis, 24,
            6))
        )
