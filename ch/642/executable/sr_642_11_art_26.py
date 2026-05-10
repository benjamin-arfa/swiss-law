"""SR 642.11 Art. 26

Generated from: ch/642/fr/642.11.md

Art. 26 Frais professionnels (Professional expenses):
Deductible professional expenses for employed taxpayers:
a. Commuting costs between home and workplace, up to CHF 3,300
b. Additional meal costs when eating away from home or doing shift work
c. Other expenses indispensable for the profession
d. [Repealed]

Para 2: Expenses under (b) and (c) are estimated as lump sums;
for (c) the taxpayer may justify higher actual costs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ifd_frais_deplacement_effectifs(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Actual commuting costs between home and workplace (CHF)"
    reference = "SR 642.11 Art. 26 Abs. 1 Bst. a"


class ifd_deduction_frais_deplacement(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for commuting costs, capped at maximum (CHF)"
    reference = "SR 642.11 Art. 26 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        frais = person('ifd_frais_deplacement_effectifs', period)
        plafond = parameters(period).sr_642_11.deduction_commuting_max
        return min_(frais, plafond)


class ifd_frais_repas_supplementaires(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Additional meal costs when eating away from home or shift work (CHF)"
    reference = "SR 642.11 Art. 26 Abs. 1 Bst. b"


class ifd_autres_frais_professionnels(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Other indispensable professional expenses (CHF)"
    reference = "SR 642.11 Art. 26 Abs. 1 Bst. c"


class ifd_deduction_frais_professionnels(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total professional expense deduction (CHF)"
    reference = "SR 642.11 Art. 26"

    def formula(person, period, parameters):
        deplacement = person('ifd_deduction_frais_deplacement', period)
        repas = person('ifd_frais_repas_supplementaires', period)
        autres = person('ifd_autres_frais_professionnels', period)
        return deplacement + repas + autres
