"""SR 952.0 Art. 37h-37j - Garantie des depots (Deposit Guarantee)

Generated from: ch/952/fr/952.0.md

Deposit guarantee system (Art. 37h):
- Banks must guarantee privileged deposits at Swiss counters
- Must adhere to self-regulation system approved by FINMA
- Guarantee body must reimburse within 7 working days of FINMA notification
- Bank contributions: total 1.6% of guaranteed deposits, minimum CHF 6 billion
- Each bank must deposit half as high-quality securities or Swiss franc cash,
  or grant a cash loan to the guarantee body for the other half

Implementation (Art. 37i):
- FINMA notifies guarantee body after protective measures or bankruptcy order
- Guarantee body provides funds within 7 working days

Reimbursement (Art. 37j):
- Plan based on depositor list
- Depositors reimbursed within 7 working days of receiving payment instructions
- If insufficient funds: pro rata reimbursement
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

TAUX_CONTRIBUTION_GARANTIE = 0.016  # 1.6%
CONTRIBUTION_MINIMALE_TOTALE = 6000000000  # CHF 6 milliards
DELAI_REMBOURSEMENT_JOURS_OUVRABLES = 7


class lb_somme_depots_garantis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Somme des depots garantis de la banque (en francs)"
    reference = "SR 952.0 Art. 37h al. 3 let. b"


class lb_contribution_garantie_depots(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Contribution de la banque au systeme de garantie des depots"
    reference = "SR 952.0 Art. 37h al. 3 let. b"

    def formula(person, period, parameters):
        depots = person('lb_somme_depots_garantis', period)
        # 1.6% des depots garantis
        return depots * TAUX_CONTRIBUTION_GARANTIE


class lb_moitie_contribution_titres(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Moitie de la contribution a deposer en titres/especes (50%)"
    reference = "SR 952.0 Art. 37h al. 3 let. c ch. 1"

    def formula(person, period, parameters):
        contribution = person('lb_contribution_garantie_depots', period)
        return contribution * 0.5


class lb_taux_couverture_depots_privilegies(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux de couverture des depots privilegies par des actifs en Suisse (min 125%)"
    reference = "SR 952.0 Art. 37a al. 6"


class lb_couverture_depots_suffisante(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La couverture des depots privilegies est suffisante (>= 125%)"
    reference = "SR 952.0 Art. 37a al. 6"

    def formula(person, period, parameters):
        taux = person('lb_taux_couverture_depots_privilegies', period)
        return taux >= 1.25


class lb_delai_remboursement_depots_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Delai pour le remboursement des depots garantis (7 jours ouvrables)"
    reference = "SR 952.0 Art. 37j al. 3"

    def formula(person, period, parameters):
        return person('lb_somme_depots_garantis', period.this_year) * 0 + DELAI_REMBOURSEMENT_JOURS_OUVRABLES
