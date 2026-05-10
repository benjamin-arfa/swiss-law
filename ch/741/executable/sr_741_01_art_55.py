"""SR 741.01 Art. 55 - Feststellung der Fahrunfaehigkeit

Generated from: ch/de/741/741.01.md

Blood/breath alcohol concentration thresholds:
- Angetrunkenheit (impaired): BAC >= 0.5 promille / BrAC >= 0.25 mg/l
- Qualifiziert (qualified): BAC >= 0.8 promille / BrAC >= 0.4 mg/l
- Mandatory investigation threshold: BAC >= 1.6 promille / BrAC >= 0.8 mg/l

Breath alcohol probe can be ordered for any driver or accident participant.
Blood test mandatory if non-alcohol impairment, refusal, or request.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class atemalkoholprobe_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Atemalkoholprobe durchgefuehrt wurde"
    reference = "SR 741.01 Art. 55 Abs. 1"


class blutprobe_angeordnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Blutprobe angeordnet wurde"
    reference = "SR 741.01 Art. 55 Abs. 3"


class anzeichen_nicht_alkohol_fahrunfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Anzeichen nicht-alkoholbedingter Fahrunfaehigkeit vorliegen"
    reference = "SR 741.01 Art. 55 Abs. 3 Bst. a"


class atemalkoholprobe_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob sich die Person der Atemalkoholprobe widersetzt oder entzieht"
    reference = "SR 741.01 Art. 55 Abs. 3 Bst. b"


class blutalkoholanalyse_verlangt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine Blutalkoholanalyse verlangt"
    reference = "SR 741.01 Art. 55 Abs. 3 Bst. c"


class blutprobe_obligatorisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Blutprobe obligatorisch angeordnet werden muss"
    reference = "SR 741.01 Art. 55 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('anzeichen_nicht_alkohol_fahrunfaehigkeit', period)
            + person('atemalkoholprobe_verweigert', period)
            + person('blutalkoholanalyse_verlangt', period)
        ) > 0


class bak_schwellenwert_angetrunken(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwellenwert fuer Angetrunkenheit (Blutalkohol in Promille)"
    reference = "SR 741.01 Art. 55 Abs. 6 Bst. a"

    def formula(person, period, parameters):
        return 0.5


class bak_schwellenwert_qualifiziert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwellenwert fuer qualifizierte Alkoholkonzentration (Blut in Promille)"
    reference = "SR 741.01 Art. 55 Abs. 6 Bst. b"

    def formula(person, period, parameters):
        return 0.8


class fahreignungsuntersuchung_schwelle_promille(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "BAC-Schwelle fuer obligatorische Fahreignungsuntersuchung (Art. 15d)"
    reference = "SR 741.01 Art. 15d Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 1.6
