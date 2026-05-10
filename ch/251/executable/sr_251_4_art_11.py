"""SR 251.4 Art. 11

Generated from: ch/251/de/251.4.md

Inhalt der Meldung: Marktanteilsschwellen die eine Meldepflicht
ausloesen (20% gemeinsamer Marktanteil, 30% einzelner Marktanteil).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gemeinsamer_marktanteil_schweiz_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gemeinsamer Marktanteil in der Schweiz von zwei oder mehr beteiligten Unternehmen in Prozent"
    reference = "SR 251.4 Art. 11 Abs. 1 Bst. d"


class einzelner_marktanteil_schweiz_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Marktanteil in der Schweiz eines einzelnen beteiligten Unternehmens in Prozent"
    reference = "SR 251.4 Art. 11 Abs. 1 Bst. d"


class markt_ist_betroffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Markt vom Zusammenschluss betroffen ist (20% gemeinsam oder 30% einzeln)"
    reference = "SR 251.4 Art. 11 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        gemeinsam = person('gemeinsamer_marktanteil_schweiz_prozent', period)
        einzeln = person('einzelner_marktanteil_schweiz_prozent', period)
        return (gemeinsam >= 20) + (einzeln >= 30)
