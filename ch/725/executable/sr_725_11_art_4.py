"""SR 725.11 Art. 4

Generated from: ch/725/de/725.11.md

Nationalstrassen dritter Klasse: Auch anderen Strassenbenützern offen.
Ortsdurchfahrten und hoehengleiche Kreuzungen sind, wo die Verhaeltnisse
es gestatten, zu vermeiden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_nationalstrasse_dritte_klasse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse eine Nationalstrasse dritter Klasse ist"
    reference = "SR 725.11 Art. 4"

    def formula(person, period, parameters):
        ist_ns = person('ist_nationalstrasse', period)
        nur_motor = person('nur_motorfahrzeuge_zugelassen', period)

        # Dritte Klasse: auch anderen Strassenbenützern offen
        return ist_ns * (1 - nur_motor)
