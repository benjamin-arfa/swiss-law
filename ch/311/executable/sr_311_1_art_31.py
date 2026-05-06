"""SR 311.1 Art. 31

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class rueckversetzung_verjaehrung_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist nach Ablauf der Probezeit, nach der keine Rueckversetzung mehr moeglich ist (2 Jahre)"
    reference = "SR 311.1 Art. 31 Abs. 4"
    default_value = 2


class probezeit_verlaengerung_max_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Verlaengerung der Probezeit (1 Jahr)"
    reference = "SR 311.1 Art. 31 Abs. 3"
    default_value = 1
