"""SR 0.101.3 Art. 1

Generated from: ch/0/de/0.101.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

def legal_article_1_participants(var):
    # Implementation of the logic based on paragraphs (1), (2), and (3)
    # We'll assume that var contains the person's characteristics

    # Condition 1: Participants in the procedure (paragraph 1(a))
    condition_participants = var.is_participant()

    # Condition 2: Witnesses, experts or other individuals able to participate (paragraph 1(b))
    condition_witnesses = var.is_witness() or var.is_expert() or var.is_able_to_participate()

    # Condition 3: Request by the Ministerkomitee (paragraph 3)
    condition_ministerkomitee = var.has_been_requested_by_ministerkomitee()

    return condition_participants or condition_witnesses or condition_ministerkomitee

# Define the OpenFisca variable
class LegalArticle1Participants(variables.IntegerVariable):
    value_type = bool
    label = "Participants of the legal article 1"
    entity = Person
    definition_period = "D"

    def formula(var, state, params):
        return legal_article_1_participants(var)
