"""SR 192.126 Art. 58

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unfallversicherung_obligatorisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Obligatorische Unfallversicherung fuer private Hausangestellte (Art. 58)"
    reference = "SR 192.126 Art. 58"

    def formula(person, period, parameters):
        # Art. 58: Arbeitgeber muss private Hausangestellte gegen Unfall versichern (UVG)
        return person('erfuellt_allgemeine_voraussetzungen', period) * 1
