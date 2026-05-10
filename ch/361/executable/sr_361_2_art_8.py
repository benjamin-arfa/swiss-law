"""SR 361.2 Art. 8

Generated from: ch/361/de/361.2.md

Weitere Bestimmungen zur Weitergabe von Daten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ipas_verwertungsverbot_besteht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwertungsverbot fuer die Daten besteht"
    reference = "SR 361.2 Art. 8 Abs. 1"


class ipas_ueberwiegende_interessen_entgegenstehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberwiegende oeffentliche oder private Interessen stehen der Weitergabe entgegen"
    reference = "SR 361.2 Art. 8 Abs. 2"


class ipas_weitergabe_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Weitergabe von IPAS-Daten wird verweigert"
    reference = "SR 361.2 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        interessen = person('ipas_ueberwiegende_interessen_entgegenstehen', period)
        return interessen
