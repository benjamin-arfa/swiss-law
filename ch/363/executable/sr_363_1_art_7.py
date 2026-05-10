"""SR 363.1 Art. 7

Generated from: ch/363/de/363.1.md

Weiterverwendung eines bereits vorhandenen DNA-Personenprofils.
Frist: 6 Monate ab erkennungsdienstlicher Erfassung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class personenprofil_bereits_gespeichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bereits im Informationssystem gespeichertes Personenprofil vorhanden"
    reference = "SR 363.1 Art. 7"


class monate_seit_erkennungsdienstlicher_erfassung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Monate seit der erkennungsdienstlichen Erfassung"
    reference = "SR 363.1 Art. 7"


class weiterverwendung_meldefrist_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Meldefrist von 6 Monaten fuer Weiterverwendung des Personenprofils eingehalten"
    reference = "SR 363.1 Art. 7"

    def formula(person, period, parameters):
        gespeichert = person('personenprofil_bereits_gespeichert', period)
        monate = person('monate_seit_erkennungsdienstlicher_erfassung', period)
        return gespeichert * (monate <= 6)
