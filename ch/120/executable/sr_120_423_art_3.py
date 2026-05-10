"""SR 120.423 Art. 3

Generated from: ch/120/de/120.423.md

Uebergangsbestimmung: Fuer Personen in Funktionen, fuer die bisher
keine oder eine niedrigere Personensicherheitspruefung erforderlich
war, muss die neue Pruefung innerhalb eines Monats eingeleitet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bisherige_pruefstufe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Bisherige Pruefstufe der Personensicherheitspruefung (0 = keine)"
    reference = "SR 120.423 Art. 3"


class neue_pruefstufe_hoeher(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die neu vorgeschriebene Pruefstufe hoeher ist als die bisherige"
    reference = "SR 120.423 Art. 3"

    def formula(person, period, parameters):
        bisherige = person('bisherige_pruefstufe', period)
        neue = person('pruefstufe_personensicherheitspruefung', period)
        return neue > bisherige


class einleitungsfrist_neue_pruefung_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist in Monaten zur Einleitung der neu vorgeschriebenen Personensicherheitspruefung"
    reference = "SR 120.423 Art. 3"

    def formula(person, period, parameters):
        return where(
            person('neue_pruefstufe_hoeher', period),
            parameters(period).einleitungsfrist_neue_pruefung_monate,
            0
        )
