"""SR 235.1 Art. 26a

Generated from: ch/235/de/235.1.md

Wiederwahl und Beendigung der Amtsdauer des Beauftragten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_beauftragter_bisherige_verlaengerungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl bisheriger Verlaengerungen der Amtsdauer"
    reference = "SR 235.1 Art. 26a Abs. 1"


class dsg_beauftragter_max_verlaengerungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anzahl Verlaengerungen der Amtsdauer"
    reference = "SR 235.1 Art. 26a Abs. 1"

    def formula(person, period, parameters):
        return person('dsg_beauftragter_bisherige_verlaengerungen', period) * 0 + 2


class dsg_beauftragter_verlaengerung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verlaengerung der Amtsdauer ist moeglich"
    reference = "SR 235.1 Art. 26a Abs. 1"

    def formula(person, period, parameters):
        bisherige = person('dsg_beauftragter_bisherige_verlaengerungen', period)
        return bisherige < 2


class dsg_kuendigungsfrist_beauftragter_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kuendigungsfrist fuer Entlassungsgesuch des Beauftragten in Monaten"
    reference = "SR 235.1 Art. 26a Abs. 2"

    def formula(person, period, parameters):
        return person('dsg_kuendigungsfrist_beauftragter_monate', period) * 0 + 6


class dsg_nichtverlagerung_frist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Verfuegung der Nichtverlaengerung vor Ablauf der Amtsdauer in Monaten"
    reference = "SR 235.1 Art. 26a Abs. 1bis"

    def formula(person, period, parameters):
        return person('dsg_nichtverlagerung_frist_monate', period) * 0 + 6
