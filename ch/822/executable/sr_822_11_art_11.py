"""SR 822.11 Art. 11

Generated from: ch/822/de/822.11.md

Art. 11: Ausgleich bei kurzfristiger Aussetzung der Arbeit -
When work is suspended temporarily (operational disruptions, company holidays),
the employer may order compensatory work deviating from the weekly maximum,
but compensation per worker may not exceed 2 hours per day (including overtime).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

class arg_ausgleich_stunden_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Angeordnete Ausgleichsstunden pro Tag bei kurzfristiger Arbeitsaussetzung"
    reference = "SR 822.11 Art. 11"


class arg_ausgleich_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ausgleich bei kurzfristiger Aussetzung ist zulaessig (max. 2h/Tag inkl. Ueberzeit)"
    reference = "SR 822.11 Art. 11"

    def formula(person, period, parameters):
        ausgleich = person('arg_ausgleich_stunden_tag', period)

        # Der Ausgleich darf, mit Einschluss von Ueberzeitarbeit,
        # zwei Stunden im Tag nicht ueberschreiten
        max_ausgleich_pro_tag = 2.0
        return ausgleich <= max_ausgleich_pro_tag
