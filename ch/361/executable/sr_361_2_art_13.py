"""SR 361.2 Art. 13

Generated from: ch/361/de/361.2.md

Protokollierung: Jede Bearbeitung festhalten, Aufbewahrung 1 Jahr.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ipas_protokollierung_aufbewahrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsdauer der Protokollierung von IPAS-Datenbearbeitungen in Jahren"
    reference = "SR 361.2 Art. 13"

    def formula(person, period, parameters):
        return person('ipas_protokollierung_aufbewahrung_jahre', period) * 0 + 1
