"""SR 170.512 Art. 1a

Generated from: ch/170/de/170.512.md

Online-Veröffentlichung: Zentrale Publikationsplattform.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class veroeffentlichung_erfolgt_online(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Veröffentlichung erfolgt über die öffentlich zugängliche Publikationsplattform (Art. 1a Abs. 1 PublG)"
    reference = "SR 170.512, Art. 1a Abs. 1"

    def formula(person, period, parameters):
        # Die Veröffentlichung erfolgt zentral online
        return person('veroeffentlichung_erfolgt_online', period) * 0 + 1


class veroeffentlichung_maschinenlesbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Veröffentlichung erfolgt maschinenlesbar mit Zugang zu allen Fassungen (Art. 1a Abs. 2 PublG)"
    reference = "SR 170.512, Art. 1a Abs. 2"
