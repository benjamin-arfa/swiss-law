"""SR 171.13 Art. 28a

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class frist_behandlung_motion_sessionen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in ordentlichen Sessionen für die abschliessende Behandlung einer Motion oder eines Kommissionspostulats"
    reference = "SR 171.13 Art. 28a Abs. 1"

    def formula(person, period, parameters):
        return 2
