"""SR 192.126 Art. 10

Generated from: ch/192/de/192.126.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_arbeitsvertrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat einen schriftlichen Arbeitsvertrag"
    reference = "SR 192.126 Art. 10"

class arbeitsvertrag_in_verstaendlicher_sprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Arbeitsvertrag ist in einer fuer die Person verstaendlichen Sprache abgefasst"
    reference = "SR 192.126 Art. 10"
