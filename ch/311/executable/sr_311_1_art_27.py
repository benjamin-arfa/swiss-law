"""SR 311.1 Art. 27

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class halbgefangenschaft_max_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer des Freiheitsentzugs fuer Halbgefangenschaft (12 Monate)"
    reference = "SR 311.1 Art. 27 Abs. 1"
    default_value = 12


class tageweiser_vollzug_max_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer des Freiheitsentzugs fuer tageweisen Vollzug (1 Monat)"
    reference = "SR 311.1 Art. 27 Abs. 1"
    default_value = 1


class begleitperson_ab_freiheitsentzug_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ab welcher Freiheitsentzugsdauer ist eine Begleitperson zu bestimmen (mehr als 1 Monat)"
    reference = "SR 311.1 Art. 27 Abs. 5"
    default_value = 30
