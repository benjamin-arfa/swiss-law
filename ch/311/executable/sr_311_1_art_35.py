"""SR 311.1 Art. 35

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bedingter_vollzug_max_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer des Freiheitsentzugs fuer bedingten Vollzug (30 Monate)"
    reference = "SR 311.1 Art. 35 Abs. 1"
    default_value = 30
