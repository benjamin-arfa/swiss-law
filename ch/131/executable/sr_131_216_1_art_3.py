"""SR 131.216.1 Art. 3

Generated from: ch/131/de/131.216.1.md

Church and state: The Roman Catholic confession as majority denomination
and the Protestant Reformed confession are recognized as churches with
public-law autonomy and independent legal personality and enjoy the
protection of the state. All other religious communities are subject
to the principles of private law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class religionszugehörigkeit(Variable):
    value_type = Enum
    possible_values = [
        'römisch_katholisch',
        'evangelisch_reformiert',
        'andere_religion',
        'keine_religion'
    ]
    default_value = 'keine_religion'
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Religionszugehörigkeit der Person"
    reference = "SR 131.216.1 Art. 3"


class anerkannte_kirche_öffentlich_rechtlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einer öffentlich-rechtlich anerkannten Kirche angehört"
    reference = "SR 131.216.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        religion = person('religionszugehörigkeit', period)
        return (religion == 'römisch_katholisch') | (religion == 'evangelisch_reformiert')


class kirchenschutz_durch_staat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Religionsgemeinschaft der Person staatlichen Schutz genießt"
    reference = "SR 131.216.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return person('anerkannte_kirche_öffentlich_rechtlich', period)


class kirche_rechtspersönlichkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Religionsgemeinschaft der Person eigene Rechtspersönlichkeit besitzt"
    reference = "SR 131.216.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return person('anerkannte_kirche_öffentlich_rechtlich', period)


class privatrechtliche_religionsgemeinschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Religionsgemeinschaft der Person dem Privatrecht untersteht"
    reference = "SR 131.216.1 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        religion = person('religionszugehörigkeit', period)
        return (religion == 'andere_religion') | (religion == 'keine_religion')