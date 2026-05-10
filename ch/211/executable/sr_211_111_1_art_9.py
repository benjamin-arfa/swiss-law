"""SR 211.111.1 Art. 9

Generated from: ch/211/de/211.111.1.md

Gerichtliche Beurteilung des Entscheids der Erwachsenenschutzbehoerde:
Anfechtung innerhalb von 30 Tagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tage_seit_eroeffnung_entscheid(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage seit Eroeffnung des Entscheids der Erwachsenenschutzbehoerde"
    reference = "SR 211.111.1 Art. 9"


class anfechtung_noch_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Anfechtung des Entscheids noch moeglich ist (innerhalb 30 Tage)"
    reference = "SR 211.111.1 Art. 9"

    def formula(person, period, parameters):
        tage = person('tage_seit_eroeffnung_entscheid', period)
        return tage <= 30
