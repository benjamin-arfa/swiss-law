"""SR 171.13 Art. 3

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitglieder_provisorisches_buero(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl der vom Alterspräsidenten ernannten Mitglieder des provisorischen Büros"
    reference = "SR 171.13 Art. 3 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 8
