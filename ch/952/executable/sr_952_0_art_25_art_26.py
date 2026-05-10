"""SR 952.0 Art. 25-26 - Mesures en cas de risque d'insolvabilite

Generated from: ch/952/fr/952.0.md

Conditions for insolvency measures (Art. 25):
- Serious reasons to fear over-indebtedness or significant liquidity problems
- Or bank failed to restore equity compliance within FINMA deadline
- FINMA can order: protective measures, restructuring, or bank bankruptcy
- Protective measures can be ordered alone or with restructuring/bankruptcy

Protective measures (Art. 26):
- Instructions to bank organs
- Appointment of investigator
- Removal of organs' powers
- Revocation of audit firm
- Limitation of bank activities
- Prohibition of payments, deposits, securities transactions
- Closure of bank
- Moratorium or extension of deadlines (except for pledged claims)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lb_surendettement_craint(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Il existe des raisons serieuses de craindre un surendettement"
    reference = "SR 952.0 Art. 25 al. 1"


class lb_problemes_liquidite_importants(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque souffre de problemes de liquidite importants"
    reference = "SR 952.0 Art. 25 al. 1"


class lb_fonds_propres_non_retablis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque n'a pas retabli ses fonds propres dans le delai imparti par la FINMA"
    reference = "SR 952.0 Art. 25 al. 1"


class lb_conditions_mesures_insolvabilite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les conditions pour des mesures en cas de risque d'insolvabilite sont remplies"
    reference = "SR 952.0 Art. 25 al. 1"

    def formula(person, period, parameters):
        surendette = person('lb_surendettement_craint', period)
        liquidite = person('lb_problemes_liquidite_importants', period)
        fp_non_retablis = person('lb_fonds_propres_non_retablis', period)
        # L'une des trois conditions suffit
        return (surendette + liquidite + fp_non_retablis) > 0


class lb_type_mesure_insolvabilite(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Type de mesure ordonnee: 0=aucune, 1=protectrices, 2=assainissement, 3=faillite"
    reference = "SR 952.0 Art. 25 al. 1"


class lb_mesure_protectrice_type(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Type de mesure protectrice: 0=aucune, 1=instructions, 2=charge_enquete, 3=retrait_pouvoirs, 4=revocation_audit, 5=limitation_activite, 6=interdiction_paiements, 7=fermeture, 8=sursis"
    reference = "SR 952.0 Art. 26 al. 1"
