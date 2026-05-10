"""SR 221.214.1 Art. 28

Generated from: ch/221/fr/221.214.1.md

Credit capacity examination: amortization over 36 months baseline,
must not impact non-seizable income portion. Takes into account
actual rent, source tax, and existing obligations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lcc_revenu_mensuel_consommateur_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Revenu mensuel du consommateur en CHF"
    reference = "SR 221.214.1 Art. 28 al. 2"


class lcc_minimum_vital_mensuel_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Minimum vital mensuel (part insaisissable du revenu) en CHF"
    reference = "SR 221.214.1 Art. 28 al. 2"


class lcc_loyer_effectif_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Loyer effectivement du en CHF"
    reference = "SR 221.214.1 Art. 28 al. 3 let. a"


class lcc_impot_du_bareme_source_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Montant de l'impot du calcule selon le bareme de l'impot a la source en CHF"
    reference = "SR 221.214.1 Art. 28 al. 3 let. b"


class lcc_engagements_existants_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Engagements communiques au centre de renseignements en CHF"
    reference = "SR 221.214.1 Art. 28 al. 3 let. c"


class lcc_duree_amortissement_examen_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree d'amortissement de reference pour l'examen de capacite (36 mois)"
    reference = "SR 221.214.1 Art. 28 al. 4"

    def formula(person, period, parameters):
        return 36


class lcc_part_saisissable_mensuelle_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Part saisissable du revenu mensuel en CHF"
    reference = "SR 221.214.1 Art. 28 al. 2-3"

    def formula(person, period, parameters):
        revenu = person('lcc_revenu_mensuel_consommateur_chf', period)
        minimum_vital = person('lcc_minimum_vital_mensuel_chf', period)
        loyer = person('lcc_loyer_effectif_chf', period)
        impot = person('lcc_impot_du_bareme_source_chf', period)
        engagements = person('lcc_engagements_existants_chf', period)
        charges = minimum_vital + loyer + impot + engagements
        return max_(revenu - charges, 0)


class lcc_mensualite_credit_36_mois_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Mensualite du credit calculee sur 36 mois en CHF"
    reference = "SR 221.214.1 Art. 28 al. 4"

    def formula(person, period, parameters):
        montant = person('lcc_montant_net_credit_chf', period)
        return montant / 36


class lcc_capacite_contracter_credit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le consommateur a la capacite de contracter le credit (mensualite <= part saisissable)"
    reference = "SR 221.214.1 Art. 28 al. 2-4"

    def formula(person, period, parameters):
        mensualite = person('lcc_mensualite_credit_36_mois_chf', period)
        part_saisissable = person('lcc_part_saisissable_mensuelle_chf', period)
        return mensualite <= part_saisissable
