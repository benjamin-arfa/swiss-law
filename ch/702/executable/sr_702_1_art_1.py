"""SR 702.1 Art. 1

Generated from: ch/702/de/702.1.md

Aufgaben und Kompetenzen der Gemeinden: Municipalities deliver resident data
to BFS annually by 31 January with reference date 31 December.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gemeinde_einwohnerdaten_stichtag_tag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Stichtag fuer Einwohnerdaten (Tag im Dezember)"
    reference = "SR 702.1 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return 31  # 31. Dezember


class gemeinde_einwohnerdaten_frist_tag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Lieferung der Einwohnerdaten (Tag im Januar des Folgejahres)"
    reference = "SR 702.1 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return 31  # 31. Januar
