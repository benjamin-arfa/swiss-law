"""SR 192.126 Art. 32

Generated from: ch/192/de/192.126.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anstellungsdauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Anstellung in Monaten"
    reference = "SR 192.126 Art. 32"

class anstellung_befristet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Arbeitsvertrag ist befristet"
    reference = "SR 192.126 Art. 32"
