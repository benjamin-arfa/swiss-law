"""SR 192.126 Art. 30

Generated from: ch/192/de/192.126.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterkunft_privater_raum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Private/r Hausangestellte/r hat eigenen abschliessbaren Raum"
    reference = "SR 192.126 Art. 30"

class unterkunft_extern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Private/r Hausangestellte/r lebt ausserhalb des Haushalts"
    reference = "SR 192.126 Art. 30"
