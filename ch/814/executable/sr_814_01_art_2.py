"""SR 814.01 Art. 2

Generated from: ch/814/de/814.01.md

Verursacherprinzip: Wer Massnahmen nach diesem Gesetz verursacht, traegt
die Kosten dafuer.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class verursacht_umweltschutzmassnahmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Massnahmen nach dem Umweltschutzgesetz verursacht"
    reference = "SR 814.01 Art. 2"


class umweltschutz_kosten_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kosten der verursachten Umweltschutzmassnahmen in CHF"
    reference = "SR 814.01 Art. 2"


class traegt_kosten_verursacherprinzip(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person nach dem Verursacherprinzip die Kosten traegt"
    reference = "SR 814.01 Art. 2"

    def formula(person, period, parameters):
        return person('verursacht_umweltschutzmassnahmen', period)
