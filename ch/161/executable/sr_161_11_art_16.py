"""SR 161.11 Art. 16

Generated from: ch/161/fr/161.11.md

By-election: if a by-election is necessary, the cantonal government
invites the party mandate holder to submit a new candidate list
within 30 days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class odp_election_complementaire_necessaire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Une election complementaire est necessaire"
    reference = "SR 161.11 Art. 16"


class odp_delai_nouvelle_liste_candidats_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour remettre une nouvelle liste de candidats (30 jours)"
    reference = "SR 161.11 Art. 16"

    def formula(person, period, parameters):
        return 30
