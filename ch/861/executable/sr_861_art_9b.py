"""SR 861 Art. 9b

Generated from: ch/de/861.md

Extensions of the deadline under Art. 9a: first to 31 Jan 2023,
then to 31 Dec 2024, then to 31 Dec 2026.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class finanzhilfe_frist_verlaengerung_2023(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Frist nach Art. 9a bis zum 31. Januar 2023 verlaengert wurde"
    reference = "SR 861 Art. 9b Abs. 1"

    def formula(person, period, parameters):
        return True


class finanzhilfe_frist_verlaengerung_2024(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Frist nach Art. 9a bis zum 31. Dezember 2024 verlaengert wurde"
    reference = "SR 861 Art. 9b Abs. 2"

    def formula(person, period, parameters):
        return True


class finanzhilfe_frist_verlaengerung_2026(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Frist nach Art. 9a bis zum 31. Dezember 2026 verlaengert wurde"
    reference = "SR 861 Art. 9b Abs. 3"

    def formula(person, period, parameters):
        return True
