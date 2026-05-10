"""SR 921.552.1 Art. 8

Generated from: ch/921/de/921.552.1.md

Warenbuchhaltung der Importeure: Eingaenge, Ausgaenge und Vorraete muessen
jederzeit ersichtlich sein. Unterlagen 5 Jahre ueber Verkauf hinaus aufbewahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermehrungsgut_import_aufbewahrungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Import-Unterlagen (Jahre ueber Verkauf hinaus)"
    reference = "SR 921.552.1 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        return 5
