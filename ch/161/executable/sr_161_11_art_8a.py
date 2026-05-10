"""SR 161.11 Art. 8a

Generated from: ch/161/fr/161.11.md

Candidate list deadline: cantons must communicate to Federal Chancellery
by March 1 of election year. Cantons with only 1 National Council seat
(without tacit election) are exempt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class odp_nombre_sieges_conseil_national_canton(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de sieges au Conseil national pour le canton"
    reference = "SR 161.11 Art. 8a al. 2"


class odp_canton_connait_election_tacite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le canton connait le systeme de l'election tacite"
    reference = "SR 161.11 Art. 8a al. 2"


class odp_delai_mise_au_point_listes_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai de mise au point des listes de candidats (7 ou 14 jours)"
    reference = "SR 161.11 Art. 8a al. 1"


class odp_canton_dispense_communication_listes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le canton est dispense de communiquer la date limite de depot des listes"
    reference = "SR 161.11 Art. 8a al. 2"

    def formula(person, period, parameters):
        un_siege = person('odp_nombre_sieges_conseil_national_canton', period) == 1
        pas_tacite = not_(person('odp_canton_connait_election_tacite', period))
        return un_siege * pas_tacite
