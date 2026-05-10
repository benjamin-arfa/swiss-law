"""SR 171.13 Art. 7

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindestanzahl_zustimmung_praesidium(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestanzahl Zustimmungen für Beschlüsse des Präsidiums (3 Mitglieder)"
    reference = "SR 171.13 Art. 7 Abs. 5"

    def formula(person, period, parameters):
        return 2
