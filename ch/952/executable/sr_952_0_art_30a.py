"""SR 952.0 Art. 30a - Ajournement de la resiliation de contrats

Generated from: ch/952/fr/952.0.md

Postponement of contract termination (Art. 30a):
- FINMA can postpone:
  a) Termination of contracts and exercise of termination rights
  b) Exercise of compensation, realization, and transfer rights (Art. 27)
- Postponement only if measures justify the termination/exercise
- Maximum 2 working days
- FINMA sets start and end of postponement
- Excluded/lapsed if termination is:
  a) Unrelated to the measures, AND
  b) Due to behavior of the bank or successor entity
- If conditions are met after postponement expires, contract continues
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lb_ajournement_ordonne(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La FINMA a ordonne un ajournement de la resiliation de contrats"
    reference = "SR 952.0 Art. 30a al. 1"


class lb_ajournement_duree_max_jours_ouvrables(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Duree maximale de l'ajournement (2 jours ouvrables)"
    reference = "SR 952.0 Art. 30a al. 3"

    def formula(person, period, parameters):
        ordonne = person('lb_ajournement_ordonne', period)
        # Maximum 2 jours ouvrables si ajournement ordonne
        return where(ordonne, 2, 0)


class lb_resiliation_liee_aux_mesures(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La resiliation est en rapport avec les mesures ordonnees"
    reference = "SR 952.0 Art. 30a al. 4 let. a"


class lb_resiliation_due_comportement_banque(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La resiliation est due au comportement de la banque"
    reference = "SR 952.0 Art. 30a al. 4 let. b"


class lb_ajournement_exclu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "L'ajournement est exclu ou caduc"
    reference = "SR 952.0 Art. 30a al. 4"

    def formula(person, period, parameters):
        liee = person('lb_resiliation_liee_aux_mesures', period)
        comportement = person('lb_resiliation_due_comportement_banque', period)
        # Exclu si: pas en rapport avec les mesures ET du au comportement de la banque
        return not_(liee) * comportement
