"""SR 192.126 Art. 57

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class krankenversicherung_obligatorisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Obligatorische Krankenversicherung fuer private Hausangestellte (Art. 57)"
    reference = "SR 192.126 Art. 57"

    def formula(person, period, parameters):
        # Art. 57: Obligatorische Krankenversicherung gemaess KVG
        return person('erfuellt_allgemeine_voraussetzungen', period) * 1
