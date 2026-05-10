"""SR 842 Art. 12

Generated from: ch/fr/842.md

Art. 12: Prets sans interet ou a taux preferentiel pour logements locatifs.

Abs. 1: L'office peut accorder des prets si:
  a. le proprietaire dispose d'un capital propre d'un certain montant
  b. les loyers sont fixes sur la base des couts pour tout l'immeuble

Abs. 2: Exemption/reduction d'interets si:
  a. revenu et fortune des locataires ne depassent pas certaines limites
  b. les logements sont occupes de maniere adequate
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class log_capital_propre_proprietaire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capital propre du proprietaire (CHF)"
    reference = "SR 842 Art. 12 al. 1 let. a"


class log_loyers_bases_sur_couts(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les loyers sont fixes sur la base des couts pour tout l'immeuble"
    reference = "SR 842 Art. 12 al. 1 let. b"


class log_revenu_locataire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Revenu du locataire (CHF)"
    reference = "SR 842 Art. 12 al. 2 let. a"


class log_fortune_locataire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fortune du locataire (CHF)"
    reference = "SR 842 Art. 12 al. 2 let. a"


class log_logement_occupe_adequatement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le logement est occupe de maniere adequate"
    reference = "SR 842 Art. 12 al. 2 let. b"


class log_eligible_pret_locatif(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Eligible a un pret pour logement locatif (Art. 12 al. 1)"
    reference = "SR 842 Art. 12 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        capital = person('log_capital_propre_proprietaire', period)
        loyers_couts = person('log_loyers_bases_sur_couts', period)
        capital_min = p.sr_842.art_12.capital_propre_min
        return (capital >= capital_min) * loyers_couts


class log_eligible_reduction_interets(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Eligible a une reduction d'interets (Art. 12 al. 2)"
    reference = "SR 842 Art. 12 al. 2"

    def formula(person, period, parameters):
        p = parameters(period)
        revenu = person('log_revenu_locataire', period)
        fortune = person('log_fortune_locataire', period)
        occupation = person('log_logement_occupe_adequatement', period)
        revenu_max = p.sr_842.art_12.revenu_locataire_max
        fortune_max = p.sr_842.art_12.fortune_locataire_max
        return (revenu <= revenu_max) * (fortune <= fortune_max) * occupation
