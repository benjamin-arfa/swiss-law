"""SR 232.119 Art. 3

Generated from: ch/232/de/232.119.md

Art. 3 regulates the conditions under which the Swiss name, Swiss cross,
and related designations may be used on watches and movements.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class darf_schweizer_bezeichnung_auf_uhr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Darf die Bezeichnung 'Schweiz', 'Swiss Made' etc. auf der Uhr anbringen"
    reference = "SR 232.119 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: nur fuer Schweizer Uhren und schweizerische Uhrwerke
        return person('ist_schweizer_uhr', period)


class darf_schweizerisches_werk_angabe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Darf die Angabe 'Schweizerisches Werk' / 'Swiss Movement' auf der Uhr anbringen"
    reference = "SR 232.119 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 3: erlaubt wenn Uhr ein schweizerisches Werk enthaelt
        return person('ist_schweizerisches_uhrwerk', period)


class darf_schweizer_bezeichnung_auf_nicht_sichtbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Darf Schweizer Bezeichnung auf dem Werk anbringen (nicht sichtbar fuer Kaeufer)"
    reference = "SR 232.119 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        # Art. 3 Abs. 2: wenn die Uhr nicht schweizerisch ist, duerfen die
        # Bezeichnungen dennoch auf schweizerischen Werken angebracht werden,
        # sofern sie fuer den Kaeufer nicht sichtbar sind
        ist_schweizer = person('ist_schweizer_uhr', period)
        werk_ch = person('ist_schweizerisches_uhrwerk', period)
        return (1 - ist_schweizer) * werk_ch
