"""SR 824.02 Art. 2

Generated from: ch/824/de/824.02.md

Umfang und Ziel der Pilotversuche: Maximum 80 deployment sites and
160 civilian service personnel for pilot projects in social welfare.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zdpv_max_einsatzbetriebe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anzahl Einsatzbetriebe fuer Pilotversuche"
    reference = "SR 824.02 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 80


class zdpv_max_zivildienstpflichtige(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anzahl zivildienstpflichtiger Personen fuer Pilotversuche"
    reference = "SR 824.02 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 160
