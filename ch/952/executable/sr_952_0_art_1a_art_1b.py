"""SR 952.0 Art. 1a-1b - Definition de banque et promotion de l'innovation

Generated from: ch/952/fr/952.0.md

Bank definition (Art. 1a):
- Anyone mainly active in financial sector who:
  a) Professionally accepts public deposits > CHF 100 million or solicits them
  b) Professionally accepts public deposits <= CHF 100 million or crypto-assets
     AND invests or remunerates them
  c) Refinances substantially from multiple non-participating banks to finance
     indeterminate persons/enterprises

Innovation promotion (Art. 1b - FinTech license):
- For entities mainly active in financial sector who:
  a) Accept professional public deposits <= CHF 100 million or designated crypto-assets
  b) Do NOT invest or remunerate these deposits/assets
- Must have: adequate organization, risk management, financial resources, fit & proper persons
- Accounts under CO only (not banking accounting rules)
- No deposit privilege (Art. 37a) or immediate reimbursement (Art. 37b)
- If exceeding CHF 100 million threshold: notify FINMA within 10 days,
  submit authorization request within 90 days
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

SEUIL_DEPOTS_BANQUE = 100000000  # CHF 100 millions
DELAI_ANNONCE_JOURS = 10
DELAI_DEMANDE_AUTORISATION_JOURS = 90


class lb_montant_depots_publics(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant des depots du public acceptes a titre professionnel (en francs)"
    reference = "SR 952.0 Art. 1a"


class lb_investit_ou_remunere_depots(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entite investit ou remunere les depots ou cryptoactifs"
    reference = "SR 952.0 Art. 1a let. b"


class lb_principalement_actif_secteur_financier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entite est principalement active dans le secteur financier"
    reference = "SR 952.0 Art. 1a"


class lb_est_banque(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entite est reputee banque au sens de l'art. 1a"
    reference = "SR 952.0 Art. 1a"

    def formula(person, period, parameters):
        financier = person('lb_principalement_actif_secteur_financier', period)
        depots = person('lb_montant_depots_publics', period)
        investit = person('lb_investit_ou_remunere_depots', period)

        # let. a: depots > 100M
        banque_a = depots > SEUIL_DEPOTS_BANQUE
        # let. b: depots <= 100M ET investit/remunere
        banque_b = (depots <= SEUIL_DEPOTS_BANQUE) * (depots > 0) * investit

        return financier * ((banque_a + banque_b) > 0)


class lb_est_fintech(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entite releve du regime fintech (art. 1b)"
    reference = "SR 952.0 Art. 1b"

    def formula(person, period, parameters):
        financier = person('lb_principalement_actif_secteur_financier', period)
        depots = person('lb_montant_depots_publics', period)
        investit = person('lb_investit_ou_remunere_depots', period)

        # Depots <= 100M ET n'investit pas / ne remunere pas
        return financier * (depots <= SEUIL_DEPOTS_BANQUE) * (depots > 0) * not_(investit)


class lb_depassement_seuil_100m(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entite depasse le seuil de 100 millions de francs"
    reference = "SR 952.0 Art. 1b al. 6"

    def formula(person, period, parameters):
        depots = person('lb_montant_depots_publics', period)
        return depots > SEUIL_DEPOTS_BANQUE


class lb_delai_annonce_finma_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour annoncer le depassement a la FINMA (10 jours)"
    reference = "SR 952.0 Art. 1b al. 6"

    def formula(person, period, parameters):
        depasse = person('lb_depassement_seuil_100m', period)
        return where(depasse, DELAI_ANNONCE_JOURS, 0)


class lb_delai_demande_autorisation_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour presenter une demande d'autorisation (90 jours)"
    reference = "SR 952.0 Art. 1b al. 6"

    def formula(person, period, parameters):
        depasse = person('lb_depassement_seuil_100m', period)
        return where(depasse, DELAI_DEMANDE_AUTORISATION_JOURS, 0)
