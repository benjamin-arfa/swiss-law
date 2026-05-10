"""SR 952.0 Art. 30b - Mesures de capitalisation (Capitalization Measures / Bail-in)

Generated from: ch/952/fr/952.0.md

Capitalization measures in restructuring plan (Art. 30b):
- Can reduce existing equity and create new equity
- Can convert third-party funds to equity and reduce claims
- Former owners have no subscription rights

Excluded from conversion/reduction:
  a) First and second class privileged claims (within privilege limits)
  b) Covered claims (within coverage limits)
  c) Offsettable claims (within offsetting conditions)
  d) Claims from obligations contracted with FINMA approval during measures

Bail-in order (Art. 30b al. 7):
  1. Subordinated claims
  2. Bail-in bonds (subject to al. 8)
  3. Other claims (except deposits)
  4. Deposits

Prerequisites (Art. 30b al. 5):
  - Convertible capital (Art. 11 al. 1 let. b) fully converted
  - Write-down bonds (Art. 11 al. 2) fully reduced
  - Share capital fully reduced
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lb_rang_creance(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Rang de la creance pour bail-in: 1=subordonnee, 2=bail-in_bonds, 3=autres, 4=depots"
    reference = "SR 952.0 Art. 30b al. 7"


class lb_creance_privilegiee_1ere_2eme_classe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La creance est privilegiee de 1ere ou 2eme classe (exclue du bail-in)"
    reference = "SR 952.0 Art. 30b al. 3 let. a"


class lb_creance_couverte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La creance est couverte (exclue du bail-in dans la limite de la couverture)"
    reference = "SR 952.0 Art. 30b al. 3 let. b"


class lb_creance_compensable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La creance est compensable (exclue du bail-in)"
    reference = "SR 952.0 Art. 30b al. 3 let. c"


class lb_creance_approuvee_finma(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La creance est nee d'engagements approuves par la FINMA (exclue du bail-in)"
    reference = "SR 952.0 Art. 30b al. 3 let. d"


class lb_creance_exclue_bail_in(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La creance est exclue de la conversion/reduction (bail-in)"
    reference = "SR 952.0 Art. 30b al. 3"

    def formula(person, period, parameters):
        priv = person('lb_creance_privilegiee_1ere_2eme_classe', period)
        couv = person('lb_creance_couverte', period)
        comp = person('lb_creance_compensable', period)
        finma = person('lb_creance_approuvee_finma', period)
        return (priv + couv + comp + finma) > 0


class lb_capital_convertible_entierement_converti(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le capital convertible (art. 11 al. 1 let. b) est entierement converti"
    reference = "SR 952.0 Art. 30b al. 5 let. a"


class lb_capital_social_entierement_reduit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le capital social est entierement reduit"
    reference = "SR 952.0 Art. 30b al. 5 let. b"


class lb_bail_in_conditions_prealables_remplies(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les conditions prealables pour le bail-in sont remplies"
    reference = "SR 952.0 Art. 30b al. 5"

    def formula(person, period, parameters):
        converti = person('lb_capital_convertible_entierement_converti', period)
        reduit = person('lb_capital_social_entierement_reduit', period)
        return converti * reduit
