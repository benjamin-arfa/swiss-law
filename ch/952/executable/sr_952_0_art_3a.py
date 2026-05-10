"""SR 952.0 Art. 3a - Banque cantonale (Cantonal Bank)

Generated from: ch/952/fr/952.0.md

Definition of cantonal bank (Art. 3a):
- Created by cantonal legislative act
- Legal form: public-law institution OR joint-stock company (SA)
- Canton must hold more than one-third of the capital AND voting rights
- Canton may guarantee all or part of the bank's liabilities
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

SEUIL_PARTICIPATION_CANTONALE = 1 / 3  # Plus d'un tiers


class lb_creee_par_acte_cantonal(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque est creee en vertu d'un acte legislatif cantonal"
    reference = "SR 952.0 Art. 3a"


class lb_participation_canton_capital(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Part du canton dans le capital (0 a 1)"
    reference = "SR 952.0 Art. 3a"


class lb_participation_canton_droits_vote(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Part du canton dans les droits de vote (0 a 1)"
    reference = "SR 952.0 Art. 3a"


class lb_est_banque_cantonale(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque est reputee banque cantonale"
    reference = "SR 952.0 Art. 3a"

    def formula(person, period, parameters):
        acte = person('lb_creee_par_acte_cantonal', period)
        capital = person('lb_participation_canton_capital', period)
        votes = person('lb_participation_canton_droits_vote', period)

        # Canton doit detenir > 1/3 du capital ET > 1/3 des droits de vote
        participation_suffisante = (capital > SEUIL_PARTICIPATION_CANTONALE) * \
                                   (votes > SEUIL_PARTICIPATION_CANTONALE)

        return acte * participation_suffisante


class lb_canton_garantit_engagements(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le canton garantit l'integralite ou une partie des engagements de la banque"
    reference = "SR 952.0 Art. 3a"
