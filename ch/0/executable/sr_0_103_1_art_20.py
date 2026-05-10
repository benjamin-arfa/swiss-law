"""SR 0.103.1 Art. 20

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class submitted_comment(Variable):
    value_type = bool
    entity = Nat
    definition_period = ETERNITY
    label = "State or special organization submitted a comment on a General Recommendation (Art. 20 ILO)"

    def formula(nat, period, parameters):
        # Since this is a boolean value that answers a yes/no question and no precise
        # implementation can be given based on the art. alone I'll have to take this
        # as a boolean parameter instead of calculation.
        return parameters(period).social_security.human_rights.general_recommendations_comments.submitted
