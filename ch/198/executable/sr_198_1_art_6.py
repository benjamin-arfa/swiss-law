"""SR 198.1 Art. 6

Generated from: ch/198/de/198.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class max_freiheitsstrafe_antarktis_vorsatz_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe bei vorsätzlicher Straftat nach Antarktis-Gesetz in Jahren"
    reference = "SR 198.1 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return 3


class mindestabstand_abfallentsorgung_seemeilen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestabstand in Seemeilen vom nächsten Land für Lebensmittelabfall-Entsorgung"
    reference = "SR 198.1 Art. 6 Abs. 1 Bst. h"

    def formula(person, period, parameters):
        return 12


class max_durchmesser_lebensmittelabfall_mm(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximaler Durchmesser in mm für Lebensmittelabfälle zur Meeresentsorgung"
    reference = "SR 198.1 Art. 6 Abs. 1 Bst. h"

    def formula(person, period, parameters):
        return 25
