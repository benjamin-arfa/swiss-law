"""SR 732.1 Art. 6

Generated from: ch/732/de/732.1.md

Bewilligungspflichten: Umgang mit Kernmaterialien erfordert
Bewilligung. Bewilligung wird befristet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class umgang_mit_kernmaterialien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person mit Kernmaterialien umgeht"
    reference = "SR 732.1 Art. 6 Abs. 1"


class umgang_mit_nuklearen_ausruestungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person mit Materialien/Ausruestungen fuer die Kernenergienutzung umgeht"
    reference = "SR 732.1 Art. 6 Abs. 2 Bst. a"


class ausfuhr_nuklearer_technologie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nukleare Technologie ausfuehrt oder vermittelt"
    reference = "SR 732.1 Art. 6 Abs. 2 Bst. b"


class bewilligung_kernmaterial_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Bewilligung fuer den Umgang mit nuklearen Guetern erforderlich ist"
    reference = "SR 732.1 Art. 6"

    def formula(person, period, parameters):
        kernmat = person('umgang_mit_kernmaterialien', period)
        ausruestung = person('umgang_mit_nuklearen_ausruestungen', period)
        tech_export = person('ausfuhr_nuklearer_technologie', period)

        return kernmat + ausruestung + tech_export > 0
