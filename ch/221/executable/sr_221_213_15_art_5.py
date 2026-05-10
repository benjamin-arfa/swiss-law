"""SR 221.213.15 Art. 5

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rahmenmietvertrag_allgemeinverbindlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag ist allgemeinverbindlich erklärt"
    reference = "SR 221.213.15 Art. 5 Abs. 1"


class einzelmietvertrag_widerspricht_rahmenmietvertrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einzelmietvertrag widerspricht allgemeinverbindlichen Bestimmungen"
    reference = "SR 221.213.15 Art. 5 Abs. 2"


class einzelmietvertrag_fuer_mietende_guenstiger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abweichende Bestimmung ist für die Mietenden günstiger"
    reference = "SR 221.213.15 Art. 5 Abs. 2"


class einzelmietvertrag_bestimmung_nichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bestimmung im Einzelmietvertrag ist nichtig"
    reference = "SR 221.213.15 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        allgemeinverbindlich = person('rahmenmietvertrag_allgemeinverbindlich', period)
        widerspricht = person('einzelmietvertrag_widerspricht_rahmenmietvertrag', period)
        guenstiger = person('einzelmietvertrag_fuer_mietende_guenstiger', period)
        return allgemeinverbindlich * widerspricht * not_(guenstiger)
