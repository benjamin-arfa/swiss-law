"""SR 741.01 Art. 95 - Fahren ohne Berechtigung

Generated from: ch/de/741/741.01.md

Driving without authorization:
- Abs. 1: Freiheitsstrafe bis 3 Jahre / Geldstrafe
  (no license, revoked license, expired probation, no learner permit)
- Abs. 2: Geldstrafe (expired probation validity)
- Abs. 3: Busse (violating conditions, unauthorized instruction)
- Abs. 4: Busse (cycling/animal when banned)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahren_ohne_fuehrerausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Motorfahrzeug ohne erforderlichen Fuehrerausweis gefuehrt wird"
    reference = "SR 741.01 Art. 95 Abs. 1 Bst. a"


class fahren_trotz_entzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob trotz Entzug oder Verweigerung des Ausweises gefahren wird"
    reference = "SR 741.01 Art. 95 Abs. 1 Bst. b"


class fahren_trotz_verfall_probeausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob trotz Verfall des Fuehrerausweises auf Probe gefahren wird"
    reference = "SR 741.01 Art. 95 Abs. 1 Bst. c"


class fahren_ohne_lernfahrausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ohne Lernfahrausweis oder ohne Begleitung Lernfahrten ausgefuehrt werden"
    reference = "SR 741.01 Art. 95 Abs. 1 Bst. d"


class fahrzeug_ueberlassen_ohne_ausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Fahrzeug einem Fahrer ohne Ausweis ueberlassen wird"
    reference = "SR 741.01 Art. 95 Abs. 1 Bst. e"


class art95_abs1_tatbestand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Tatbestand nach Art. 95 Abs. 1 SVG erfuellt ist"
    reference = "SR 741.01 Art. 95 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('fahren_ohne_fuehrerausweis', period)
            + person('fahren_trotz_entzug', period)
            + person('fahren_trotz_verfall_probeausweis', period)
            + person('fahren_ohne_lernfahrausweis', period)
            + person('fahrzeug_ueberlassen_ohne_ausweis', period)
        ) > 0


class art95_strafe_freiheitsstrafe_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Freiheitsstrafe nach Art. 95 SVG in Jahren"
    reference = "SR 741.01 Art. 95"

    def formula(person, period, parameters):
        abs1 = person('art95_abs1_tatbestand', period)
        return where(abs1, 3, 0)
