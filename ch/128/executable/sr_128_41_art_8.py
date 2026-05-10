"""SR 128.41 Art. 8

Generated from: ch/128/de/128.41.md

Meldung geeigneter Betriebe: The contracting authority may report up to 5
eligible enterprises. A higher number requires justification.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_gemeldete_betriebe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl der gemeldeten in Frage kommenden Betriebe"
    reference = "SR 128.41 Art. 8 Abs. 1"


class begruendung_fuer_mehr_als_5_betriebe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Begruendung fuer die Zulassung von mehr als 5 Betrieben vorliegt"
    reference = "SR 128.41 Art. 8 Abs. 1"


class meldung_betriebe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Meldung der Anzahl Betriebe zulaessig ist"
    reference = "SR 128.41 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('anzahl_gemeldete_betriebe', period)
        begruendung = person('begruendung_fuer_mehr_als_5_betriebe', period)
        return (anzahl <= 5) + ((anzahl > 5) * begruendung) > 0
