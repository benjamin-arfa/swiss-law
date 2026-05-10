"""SR 291 Art. 10

Generated from: ch/291/de/291.md

Vorsorgliche Massnahmen: Zustaendig zur Anordnung vorsorglicher Massnahmen
sind die schweizerischen Gerichte oder Behoerden, die in der Hauptsache
zustaendig sind, oder die Gerichte und Behoerden am Ort, an dem die
Massnahme vollstreckt werden soll.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gericht_in_hauptsache_zustaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das schweizerische Gericht in der Hauptsache zustaendig ist"
    reference = "SR 291 Art. 10 lit. a"


class massnahme_am_vollstreckungsort(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Massnahme am schweizerischen Vollstreckungsort vollstreckt werden soll"
    reference = "SR 291 Art. 10 lit. b"


class zustaendig_fuer_vorsorgliche_massnahmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein schweizerisches Gericht fuer vorsorgliche Massnahmen zustaendig ist"
    reference = "SR 291 Art. 10"

    def formula(person, period, parameters):
        hauptsache = person('gericht_in_hauptsache_zustaendig', period)
        vollstreckungsort = person('massnahme_am_vollstreckungsort', period)
        return hauptsache + vollstreckungsort > 0
