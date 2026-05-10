"""SR 844 Art. 9

Generated from: ch/fr/844.md

Art. 9: Imputation des prestations de tiers.

Abs. 1: Les prestations de communes, autres cantons, collectivites,
employeurs, fondations ou institutions d'utilite publique peuvent
etre imputees sur la contribution cantonale, mais ne peuvent
remplacer la contribution du canton que jusqu'a concurrence
de quatre cinquiemes (4/5).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lalm_prestations_tiers(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prestations de tiers imputables sur la contribution cantonale (CHF)"
    reference = "SR 844 Art. 9 al. 1"


class lalm_part_maximale_tiers(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Part maximale des prestations de tiers dans la contribution cantonale (CHF)"
    reference = "SR 844 Art. 9 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        prestation_canton = person('lalm_prestation_canton_minimale', period)
        ratio_max = p.sr_844.art_9.ratio_max_tiers
        return prestation_canton * ratio_max


class lalm_prestations_tiers_imputables(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant effectivement imputable des prestations de tiers (CHF)"
    reference = "SR 844 Art. 9 al. 1"

    def formula(person, period, parameters):
        prestations = person('lalm_prestations_tiers', period)
        plafond = person('lalm_part_maximale_tiers', period)
        return min_(prestations, plafond)


class lalm_contribution_canton_propre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Contribution propre minimale du canton (hors tiers, CHF)"
    reference = "SR 844 Art. 9 al. 1"

    def formula(person, period, parameters):
        prestation_canton = person('lalm_prestation_canton_minimale', period)
        tiers_imputables = person('lalm_prestations_tiers_imputables', period)
        return max_(prestation_canton - tiers_imputables, 0)
