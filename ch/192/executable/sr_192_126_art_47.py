"""SR 192.126 Art. 47

Generated from: ch/192/de/192.126.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_woechentlichen_ruhetag(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat mindestens einen vollen Ruhetag pro Woche (Art. 47)"
    reference = "SR 192.126 Art. 47"

class halber_ruhetag_pro_woche(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat zusaetzlich einen halben freien Tag pro Woche (Art. 47 Abs. 1)"
    reference = "SR 192.126 Art. 47"
