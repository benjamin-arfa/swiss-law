"""SR 442.121.1 Art. 12

Generated from: ch/442/de/442.121.1.md

Hoechstzahl der unterstuetzten Vorhaben und Ausstellungen:
- Max 25 Institutionen pro Ausschreibung mit Projektbeitraegen
- Max 6 Ausstellungen pro Jahr mit Versicherungsbeitraegen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_institutionen_mit_projektbeitraegen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Institutionen mit Projektbeitraegen pro Ausschreibung"
    reference = "SR 442.121.1 Art. 12 Abs. 1"


class anzahl_ausstellungen_mit_versicherungsbeitraegen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Ausstellungen mit Versicherungsbeitraegen pro Jahr"
    reference = "SR 442.121.1 Art. 12 Abs. 2"


class projektbeitraege_limit_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Limit von 25 Institutionen mit Projektbeitraegen eingehalten wird"
    reference = "SR 442.121.1 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('anzahl_institutionen_mit_projektbeitraegen', period)
        return anzahl <= 25


class versicherungsbeitraege_limit_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Limit von 6 Ausstellungen mit Versicherungsbeitraegen eingehalten wird"
    reference = "SR 442.121.1 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        anzahl = person('anzahl_ausstellungen_mit_versicherungsbeitraegen', period)
        return anzahl <= 6
