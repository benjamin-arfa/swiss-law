"""SR 641.811.31 Art. 3

Generated from: ch/641/de/641.811.31.md

Evidence: the applicant must prove that the heavy vehicle tax was paid.
Documents must be retained for five years and presented on demand.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class abgabe_entrichtet_nachweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Nachweis erbracht wurde dass die Schwerverkehrsabgabe entrichtet wurde"
    reference = "SR 641.811.31 Art. 3 Abs. 1"


class aufbewahrungsfrist_belege_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Unterlagen und Belege in Jahren"
    reference = "SR 641.811.31 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        return 5
