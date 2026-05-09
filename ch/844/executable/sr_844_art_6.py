"""SR 844 Art. 6

Generated from: ch/fr/844.md

Art. 6: Majoration de l'aide financiere en cas de charge excessive.

Selon la capacite financiere du canton, l'aide financiere peut etre
majoree de 5 a 15 % des frais pouvant etre pris en consideration si,
malgre les aides ordinaires de la Confederation et du canton, les travaux
imposent au requerant une charge excessive.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lalm_charge_excessive(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les travaux imposent une charge excessive au requerant"
    reference = "SR 844 Art. 6"


class lalm_taux_majoration(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux de majoration de l'aide financiere (5 a 15%)"
    reference = "SR 844 Art. 6"

    def formula(person, period, parameters):
        p = parameters(period)
        capacite = person('lalm_capacite_financiere_canton', period)
        charge_excessive = person('lalm_charge_excessive', period)
        taux_min = p.sr_844.art_6.taux_majoration_min
        taux_max = p.sr_844.art_6.taux_majoration_max
        taux = taux_max - capacite * (taux_max - taux_min)
        return where(charge_excessive, taux, 0)


class lalm_aide_financiere_majoree(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant total de l'aide financiere avec majoration (Art. 5+6, CHF)"
    reference = "SR 844 Art. 6"

    def formula(person, period, parameters):
        aide_base = person('lalm_aide_financiere_art5', period)
        frais = person('lalm_frais_pris_en_consideration', period)
        taux_maj = person('lalm_taux_majoration', period)
        majoration = frais * taux_maj
        return aide_base + majoration
