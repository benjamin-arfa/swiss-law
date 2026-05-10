"""SR 510.35 Art. 2 - Arten seuchenpolizeilicher Massnahmen

Generated from: ch/510/de/510.35.md

Als seuchenpolizeiliche Massnahmen kommen insbesondere in Betracht:
a. Sperre
b. Quarantaene
c. Verschieben oder Ausfallenlassen von militaerischen Schulen, Kursen
d. Aufgebot von Sanitaets- und Veterinaerpersonal
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sperre_angeordnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine seuchenpolizeiliche Sperre angeordnet wurde"
    reference = "SR 510.35 Art. 2 Abs. 1 lit. a"


class quarantaene_angeordnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Quarantaene angeordnet wurde"
    reference = "SR 510.35 Art. 2 Abs. 1 lit. b"


class mil_schulen_kurse_verschoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob militaerische Schulen, Kurse und Veranstaltungen verschoben oder ausgefallen sind"
    reference = "SR 510.35 Art. 2 Abs. 1 lit. c"


class sanitaetspersonal_aufgeboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Sanitaets- und Veterinaerpersonal aufgeboten wurde"
    reference = "SR 510.35 Art. 2 Abs. 1 lit. d"
