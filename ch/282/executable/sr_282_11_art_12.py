"""SR 282.11 Art. 12 - Zweckgebundenes Vermoegen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class vermoegen_ist_zweckgebunden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Vermoegen ist zugunsten Dritter zweckgebunden (Fonds, Amtskautionen, Pensionskassen)"
    reference = "SR 282.11 Art. 12 Abs. 1"


class verpflichtung_aus_zweckbestimmung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung ergibt sich aus der Zweckbestimmung des Vermoegens"
    reference = "SR 282.11 Art. 12 Abs. 1"


# Computed variables

class zweckgebundenes_vermoegen_pfaendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das zweckgebundene Vermoegen kann fuer diese Verpflichtung gepfaendet werden"
    reference = "SR 282.11 Art. 12 Abs. 1"

    def formula(self, period, parameters):
        zweckgebunden = self('vermoegen_ist_zweckgebunden', period)
        aus_zweck = self('verpflichtung_aus_zweckbestimmung', period)
        # Nur fuer Verpflichtungen aus der Zweckbestimmung pfaendbar
        return zweckgebunden * aus_zweck
