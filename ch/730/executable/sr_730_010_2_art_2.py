"""SR 730.010.2 Art. 2

Generated from: ch/730/fr/730.010.2.md

Art. 2 - Validity of guarantees of origin for fuels:
1. A guarantee of origin is valid for 18 months after the date of
   the month of its issuance.
2. During its validity, it can be cancelled and used to certify
   fuel usage (subject to other federal legislation).
3. For long-term storage, the 18-month period is suspended on request.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ogoc_date_etablissement_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Month of issuance of the guarantee of origin (1-12)"
    reference = "SR 730.010.2 Art. 2 Abs. 1"


class ogoc_stockage_long_terme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the fuel is in long-term storage (suspends validity period)"
    reference = "SR 730.010.2 Art. 2 Abs. 3"
    default_value = False


class ogoc_duree_stockage_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duration of long-term storage in months (suspends validity countdown)"
    reference = "SR 730.010.2 Art. 2 Abs. 3"
    default_value = 0


class ogoc_validite_effective_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Effective validity duration including storage suspension (months)"
    reference = "SR 730.010.2 Art. 2"

    def formula(person, period, parameters):
        stockage = person('ogoc_stockage_long_terme', period)
        duree_stockage = person('ogoc_duree_stockage_mois', period)
        p = parameters(period).sr_730_010_2

        validite_base = p.validite_go_combustible_mois

        # If in long-term storage, add storage duration to validity
        return where(stockage, validite_base + duree_stockage, validite_base)
