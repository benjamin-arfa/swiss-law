"""SR 151.3 Art. 3

Generated from: ch/151/de/151.3.md

Geltungsbereich: Das Gesetz gilt fuer bestimmte Bauten, Anlagen,
Fahrzeuge, Dienstleistungen und Arbeitsverhaeltnisse.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_oeffentlich_zugaengliche_baute(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine oeffentlich zugaengliche Baute/Anlage handelt"
    reference = "SR 151.3 Art. 3 Bst. a"


class ist_oeffentlicher_verkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Einrichtung/Fahrzeug des oeffentlichen Verkehrs handelt"
    reference = "SR 151.3 Art. 3 Bst. b"


class anzahl_wohneinheiten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Wohneinheiten im Wohngebaeude"
    reference = "SR 151.3 Art. 3 Bst. c"


class anzahl_arbeitsplaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Arbeitsplaetze im Gebaeude"
    reference = "SR 151.3 Art. 3 Bst. d"


class behig_anwendbar_wohngebaeude(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BehiG auf das Wohngebaeude anwendbar ist (mehr als 8 Wohneinheiten)"
    reference = "SR 151.3 Art. 3 Bst. c"

    def formula(person, period, parameters):
        return person('anzahl_wohneinheiten', period) > 8


class behig_anwendbar_arbeitsgebaeude(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BehiG auf das Gebaeude anwendbar ist (mehr als 50 Arbeitsplaetze)"
    reference = "SR 151.3 Art. 3 Bst. d"

    def formula(person, period, parameters):
        return person('anzahl_arbeitsplaetze', period) > 50
