"""SR 410.21 Art. 10

Generated from: ch/410/de/410.21.md

Kuendigung - Frist von zwei Jahren auf Ende einer BFI-Periode.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kuendigungsfrist_bildungszusammenarbeit_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kuendigungsfrist fuer die Vereinbarung in Jahren"
    reference = "SR 410.21 Art. 10"

    def formula(person, period):
        return 2
