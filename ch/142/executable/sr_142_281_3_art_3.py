"""SR 142.281.3 Art. 3

Generated from: ch/142/de/142.281.3.md

Zuschlag fuer Sportbauten: bei Einrichtungen ab 100 Haftplaetzen
ein Flaechenzuschlag bis max. 2.9 m2 pro Haftplatz, angerechnet dem
Bereich Insassenwesen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zuschlag_sportbauten_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Flaechenzuschlag fuer Sportbauten pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 3"

    def formula(person, period, parameters):
        anzahl = person('anzahl_haftplaetze', period)
        # Zuschlag nur bei Einrichtungen ab 100 Haftplaetzen
        return where(anzahl >= 100, 2.9, 0.0)
