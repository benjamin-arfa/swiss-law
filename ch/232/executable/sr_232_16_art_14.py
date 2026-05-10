"""SR 232.16 Art. 14

Generated from: ch/232/de/232.16.md

Art. 14 defines the duration of plant variety protection.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_rebe_oder_baum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Sorte ist eine Rebe oder ein Baum"
    reference = "SR 232.16 Art. 14"


class sortenschutz_erteilungsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kalenderjahr der Erteilung des Sortenschutzes"
    reference = "SR 232.16 Art. 14"


class sortenschutz_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Der Sortenschutz ist abgelaufen"
    reference = "SR 232.16 Art. 14"

    def formula(person, period, parameters):
        erteilungsjahr = person('sortenschutz_erteilungsjahr', period)
        rebe_baum = person('ist_rebe_oder_baum', period)
        aktuelles_jahr = period.start.year

        # Standard: 25 Jahre; Reben und Baeume: 30 Jahre
        schutzdauer = where(rebe_baum, 30, 25)
        return aktuelles_jahr > (erteilungsjahr + schutzdauer)
