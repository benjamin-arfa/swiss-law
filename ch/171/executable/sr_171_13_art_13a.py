"""SR 171.13 Art. 13a

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitglieder_immunitaetskommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der Immunitätskommission"
    reference = "SR 171.13 Art. 13a Abs. 1"

    def formula(person, period, parameters):
        return 9
