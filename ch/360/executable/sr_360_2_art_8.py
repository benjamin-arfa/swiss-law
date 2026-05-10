"""SR 360.2 Art. 8

Generated from: ch/360/de/360.2.md

Bearbeitete Daten: Einschraenkungen der Datenbearbeitung im NES.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_person_nur_drogenkonsument(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person konsumiert nur Drogen (kein Handel)"
    reference = "SR 360.2 Art. 8 Abs. 1"


class nes_drogen_daten_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Datenbearbeitung zur Drogenbekaempfung im NES ist zulaessig"
    reference = "SR 360.2 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        nur_konsument = person('nes_person_nur_drogenkonsument', period)
        # Nur Konsum = keine Registrierung im NES
        return not_(nur_konsument)
