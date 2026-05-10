"""SR 844 Art. 8

Generated from: ch/fr/844.md

Art. 8: Prestation du canton.

Abs. 1: La prestation du canton + aide financiere doivent couvrir:
  - 50% des frais dans les cas Art. 5 (aide ordinaire)
  - 75% des frais dans les cas Art. 6 (charge excessive)

Abs. 2: Si le taux d'aide est reduit (cas particulier), le canton
peut reduire sa prestation dans la meme mesure.

Abs. 3: Le canton peut subordonner sa prestation a une part communale.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lalm_prestation_canton_minimale(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prestation minimale du canton (CHF)"
    reference = "SR 844 Art. 8 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        frais = person('lalm_frais_pris_en_consideration', period)
        aide_base = person('lalm_aide_financiere_art5', period)
        charge_excessive = person('lalm_charge_excessive', period)
        taux_couverture_normal = p.sr_844.art_8.taux_couverture_normal
        taux_couverture_excessif = p.sr_844.art_8.taux_couverture_excessif
        taux = where(charge_excessive, taux_couverture_excessif, taux_couverture_normal)
        couverture_requise = frais * taux
        aide_majoree = person('lalm_aide_financiere_majoree', period)
        aide = where(charge_excessive, aide_majoree, aide_base)
        return max_(couverture_requise - aide, 0)


class lalm_couverture_totale(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Couverture totale (aide federale + prestation canton, CHF)"
    reference = "SR 844 Art. 8 al. 1"

    def formula(person, period, parameters):
        charge_excessive = person('lalm_charge_excessive', period)
        aide_base = person('lalm_aide_financiere_art5', period)
        aide_majoree = person('lalm_aide_financiere_majoree', period)
        aide = where(charge_excessive, aide_majoree, aide_base)
        prestation_canton = person('lalm_prestation_canton_minimale', period)
        return aide + prestation_canton
