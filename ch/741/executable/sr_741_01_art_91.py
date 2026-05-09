"""SR 741.01 Art. 91 - Fahren in fahrunfaehigem Zustand

Generated from: ch/de/741/741.01.md

Drunk/impaired driving penalties:
- Abs. 1: Busse (non-qualified BAC, alcohol ban violation, impaired on non-motorized)
- Abs. 2: Freiheitsstrafe bis 3 Jahre / Geldstrafe (qualified BAC or other impairment on motorized)

BAC thresholds (from Art. 55 Abs. 6):
- Angetrunkenheit: >= 0.5 Promille (Blut) / 0.25 mg/l (Atem)
- Qualifiziert: >= 0.8 Promille (Blut) / 0.4 mg/l (Atem)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class blutalkoholkonzentration_promille(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Blutalkoholkonzentration in Gewichtspromille"
    reference = "SR 741.01 Art. 55 Abs. 6"


class atemalkoholkonzentration_mg_l(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Atemalkoholkonzentration in mg/l Atemluft"
    reference = "SR 741.01 Art. 55 Abs. 6"


class ist_motorfahrzeugfuehrer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ein Motorfahrzeug fuehrt"
    reference = "SR 741.01 Art. 91"


class alkoholverbot_personengruppe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob fuer die Person ein Alkoholfahrverbot gilt (Art. 31 Abs. 2bis)"
    reference = "SR 741.01 Art. 31 Abs. 2bis"


class fahrunfaehig_andere_gruende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Fahrunfaehigkeit aus anderen Gruenden (Betaeubungsmittel etc.) vorliegt"
    reference = "SR 741.01 Art. 91 Abs. 2 Bst. b"


class angetrunken(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Angetrunkenheit vorliegt (>= 0.5 Promille oder >= 0.25 mg/l)"
    reference = "SR 741.01 Art. 55 Abs. 6"

    def formula(person, period, parameters):
        bak = person('blutalkoholkonzentration_promille', period)
        aak = person('atemalkoholkonzentration_mg_l', period)
        return (bak >= 0.5) + (aak >= 0.25) > 0


class qualifizierte_alkoholkonzentration(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine qualifizierte Alkoholkonzentration vorliegt (>= 0.8 Promille oder >= 0.4 mg/l)"
    reference = "SR 741.01 Art. 55 Abs. 6"

    def formula(person, period, parameters):
        bak = person('blutalkoholkonzentration_promille', period)
        aak = person('atemalkoholkonzentration_mg_l', period)
        return (bak >= 0.8) + (aak >= 0.4) > 0


class art91_strafe_freiheitsstrafe_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Freiheitsstrafe nach Art. 91 SVG in Jahren"
    reference = "SR 741.01 Art. 91"

    def formula(person, period, parameters):
        motor = person('ist_motorfahrzeugfuehrer', period)
        qualifiziert = person('qualifizierte_alkoholkonzentration', period)
        andere = person('fahrunfaehig_andere_gruende', period)
        # Abs. 2: bis 3 Jahre bei qualifizierter BAC + Motorfahrzeug
        # oder bei Fahrunfaehigkeit aus anderen Gruenden + Motorfahrzeug
        schwer = motor * ((qualifiziert) + (andere)) > 0
        return where(schwer, 3, 0)
