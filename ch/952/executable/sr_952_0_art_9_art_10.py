"""SR 952.0 Art. 9-10 - Exigences pour banques d'importance systemique

Generated from: ch/952/fr/952.0.md

Special requirements for systemically important banks:
- Art. 9: Must meet higher standards for equity, liquidity, risk distribution, emergency plan
  - Equity must ensure better loss-bearing capacity than non-systemic banks
  - In case of insolvency threat, equity must maintain systemic functions
  - Liquidity must ensure better shock absorption
  - Must have emergency plan for immediate implementation
- Art. 10: FINMA defines specific requirements per bank after hearing BNS
  - Bank must prove it meets emergency plan requirements
  - FINMA grants relief if bank improves its resolvability beyond requirements
- Art. 10a: If systemic bank receives state aid, Federal Council orders remuneration measures
  - Can prohibit variable remuneration entirely or partially
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lb_systemique_fonds_propres_suffisants(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque systemique dispose de fonds propres suffisants (art. 9 al. 2 let. a)"
    reference = "SR 952.0 Art. 9 al. 2 let. a"


class lb_systemique_liquidites_suffisantes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque systemique dispose de liquidites suffisantes (art. 9 al. 2 let. b)"
    reference = "SR 952.0 Art. 9 al. 2 let. b"


class lb_systemique_repartition_risques_conforme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque systemique repartit les risques conformement aux exigences (art. 9 al. 2 let. c)"
    reference = "SR 952.0 Art. 9 al. 2 let. c"


class lb_systemique_plan_urgence_existe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque systemique dispose d'un plan d'urgence (art. 9 al. 2 let. d)"
    reference = "SR 952.0 Art. 9 al. 2 let. d"


class lb_systemique_exigences_remplies(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque systemique remplit toutes les exigences particulieres"
    reference = "SR 952.0 Art. 9"

    def formula(person, period, parameters):
        fp = person('lb_systemique_fonds_propres_suffisants', period)
        liq = person('lb_systemique_liquidites_suffisantes', period)
        risques = person('lb_systemique_repartition_risques_conforme', period)
        plan = person('lb_systemique_plan_urgence_existe', period)
        return fp * liq * risques * plan


class lb_systemique_recoit_aide_etat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque systemique recoit une aide financiere de la Confederation"
    reference = "SR 952.0 Art. 10a al. 1"


class lb_systemique_remuneration_variable_interdite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les remunerations variables sont interdites (en cas d'aide etatique)"
    reference = "SR 952.0 Art. 10a al. 2 let. a"

    def formula(person, period, parameters):
        # Si aide etatique, le Conseil federal peut interdire les remunerations variables
        return person('lb_systemique_recoit_aide_etat', period)
