"""SR 901.022 Art. 11

Generated from: ch/901/fr/901.022.md

Art. 11: Montant de l'allegement fiscal.

Abs. 1: L'allegement fiscal federal = min(abattement cantonal/communal escompte,
plafond demande par le canton).

Abs. 2: Ne peut depasser le plafond fixe par la Confederation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class rpol_abattement_cantonal_communal(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abattements fiscaux escomptes aux niveaux cantonal et communal (CHF)"
    reference = "SR 901.022 Art. 11 al. 1 let. a"


class rpol_plafond_demande_canton(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Plafond demande par le canton pour l'allegement federal (CHF)"
    reference = "SR 901.022 Art. 11 al. 1 let. b"


class rpol_plafond_federal(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Plafond fixe par la Confederation pour l'allegement fiscal (CHF)"
    reference = "SR 901.022 Art. 11 al. 2"


class rpol_montant_allegement_federal(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant de l'allegement fiscal federal (CHF)"
    reference = "SR 901.022 Art. 11"

    def formula(person, period, parameters):
        abattement = person('rpol_abattement_cantonal_communal', period)
        plafond_canton = person('rpol_plafond_demande_canton', period)
        plafond_federal = person('rpol_plafond_federal', period)
        # Al. 1: min des deux montants
        montant = min_(abattement, plafond_canton)
        # Al. 2: ne peut depasser le plafond federal
        return min_(montant, plafond_federal)
