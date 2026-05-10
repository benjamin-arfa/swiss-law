"""SR 0.142.116.919 Art. 16

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liability_for_damages(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Art. 16 liability for damages"

    def formula(person, period, parameters):
        return "According to the rules set in Art. 16 of the bilateral agreement on damages caused to third parties, requesting party is liable unless claim is against the requested party, which will be liable according to its internal law"
