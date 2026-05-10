"""SR 957.1 Art. 9

Generated from: ch/957/de/957.1.md

Drittverwahrung:
- Verwahrungsstelle kann Bucheffekten durch Drittverwahrungsstelle
  in Schweiz oder Ausland verwahren lassen
- Zustimmung der Kontoinhaberin nicht erforderlich
- Ausnahme: Drittverwahrung im Ausland ohne angemessene Aufsicht
  erfordert ausdrückliche Zustimmung
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class drittverwahrung_im_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Drittverwahrung im Ausland erfolgt"
    reference = "SR 957.1 Art. 9 Abs. 2"


class drittverwahrungsstelle_angemessen_beaufsichtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ausländische Verwahrungsstelle einer angemessenen Aufsicht untersteht"
    reference = "SR 957.1 Art. 9 Abs. 2"


class ausdrueckliche_zustimmung_kontoinhaberin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ausdrückliche Zustimmung der Kontoinhaberin vorliegt"
    reference = "SR 957.1 Art. 9 Abs. 2"


class drittverwahrung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Drittverwahrung zulässig ist"
    reference = "SR 957.1 Art. 9"

    def formula(person, period, parameters):
        ausland = person('drittverwahrung_im_ausland', period)
        beaufsichtigt = person('drittverwahrungsstelle_angemessen_beaufsichtigt', period)
        zustimmung = person('ausdrueckliche_zustimmung_kontoinhaberin', period)

        # In der Schweiz: immer zulässig
        # Im Ausland mit Aufsicht: zulässig
        # Im Ausland ohne Aufsicht: nur mit Zustimmung
        return (ausland == False) + (ausland * beaufsichtigt) + (ausland * (beaufsichtigt == False) * zustimmung)
