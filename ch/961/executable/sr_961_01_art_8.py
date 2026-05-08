"""SR 961.01 Art. 8-10 — Capital minimum et fonds d'organisation

Generated from: ch/961/fr/961.01.md

LSA — Minimum capital and organization fund:
- Art. 8: Minimum capital between 3 and 20 million CHF depending on insurance branches
- Art. 9/9a: Solvency — risk-bearing capital must be >= target capital
  Target capital based on insurance, market, and credit risks
- Art. 10: Organization fund up to 50% of minimum capital at start of activity
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class capital_minimum_assurance(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capital minimum requis selon les branches d'assurance exploitées (CHF)"
    reference = "SR 961.01 Art. 8 al. 1"


class capital_effectif_assurance(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capital effectif de l'entreprise d'assurance (CHF)"
    reference = "SR 961.01 Art. 8"


class capital_minimum_respecte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le capital effectif respecte le capital minimum requis"
    reference = "SR 961.01 Art. 8"

    def formula(person, period, parameters):
        effectif = person('capital_effectif_assurance', period)
        minimum = person('capital_minimum_assurance', period)
        return effectif >= minimum


class capital_porteur_risque(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capital porteur de risque (fonds destinés à absorber les pertes) (CHF)"
    reference = "SR 961.01 Art. 9a al. 2"


class capital_cible(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capital cible basé sur les risques d'assurance, de marché et de crédit (CHF)"
    reference = "SR 961.01 Art. 9a al. 3"


class solvabilite_suffisante(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Solvabilité suffisante: capital porteur de risque >= capital cible"
    reference = "SR 961.01 Art. 9 al. 2"

    def formula(person, period, parameters):
        return person('capital_porteur_risque', period) >= person('capital_cible', period)


class fonds_organisation_requis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fonds d'organisation requis (en règle générale max 50% du capital minimum) (CHF)"
    reference = "SR 961.01 Art. 10 al. 1"

    def formula(person, period, parameters):
        capital_min = person('capital_minimum_assurance', period)
        taux = parameters(period).sr_961_01.taux_fonds_organisation_max
        return capital_min * taux


class fonds_organisation_effectif(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fonds d'organisation effectif de l'entreprise d'assurance (CHF)"
    reference = "SR 961.01 Art. 10"


class fonds_organisation_suffisant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le fonds d'organisation effectif est suffisant"
    reference = "SR 961.01 Art. 10"

    def formula(person, period, parameters):
        return person('fonds_organisation_effectif', period) >= person('fonds_organisation_requis', period)
