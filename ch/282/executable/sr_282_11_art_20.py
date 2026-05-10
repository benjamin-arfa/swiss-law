"""SR 282.11 Art. 20 - Abstimmungsquoren

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class anteil_vertretenes_kapital_zustimmend(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil des vertretenen Obligationenkapitals, das zugestimmt hat"
    reference = "SR 282.11 Art. 20 Abs. 1"


class anteil_umlaufendes_kapital_zustimmend(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil des im Umlauf befindlichen Obligationenkapitals, das zugestimmt hat"
    reference = "SR 282.11 Art. 20 Abs. 1"


# Computed variables

class beschluss_gueltig_art20(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beschluss ueber Eingriffe in Glaeubigerrechte ist gueltig (Art. 20)"
    reference = "SR 282.11 Art. 20 Abs. 1"

    def formula(self, period, parameters):
        vertreten = self('anteil_vertretenes_kapital_zustimmend', period)
        umlaufend = self('anteil_umlaufendes_kapital_zustimmend', period)
        # Zwei Drittel des vertretenen UND einfache Mehrheit des im Umlauf befindlichen
        return (vertreten >= 2/3) * (umlaufend > 0.5)
