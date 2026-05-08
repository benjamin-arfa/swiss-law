"""SR 916.010.2 Art. 3

Generated from: ch/916/fr/916.010.2.md

Disposition transitoire — Communication materials produced before 1 June 2008
may only be used after 1 January 2009 if they comply with this ordinance.
Printed materials may still be used.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from datetime import date


class support_produit_avant_juin_2008(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Communication material was produced before 1 June 2008"
    reference = "SR 916.010.2 Art. 3"


class support_est_imprime(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Communication material is printed (as opposed to digital)"
    reference = "SR 916.010.2 Art. 3"


class ancien_support_utilisable(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Pre-June-2008 communication material may still be used"
    reference = "SR 916.010.2 Art. 3"

    def formula_2008(organisation, period, parameters):
        avant_juin_2008 = organisation('support_produit_avant_juin_2008', period)
        conforme = organisation('utilise_identite_visuelle_commune', period)
        est_imprime = organisation('support_est_imprime', period)

        # After 1 Jan 2009, old materials need compliance OR be printed
        return avant_juin_2008 * (conforme + est_imprime > 0)
