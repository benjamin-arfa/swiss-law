"""SR 831.20 Art. 23bis

Generated from: ch/831/de/831.20.md

Art. 23bis: Kindergeld - Child allowance component of daily allowance:
The child allowance is 2% of the maximum daily allowance (Art. 24 Abs. 1)
per child.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_anzahl_anspruchsberechtigte_kinder_taggeld(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Anzahl Kinder mit Anspruch auf Kindergeld zum IV-Taggeld "
        "(unter 18 bzw. in Ausbildung bis 25)"
    )
    reference = "SR 831.20 Art. 22bis Abs. 2"


class iv_kindergeld_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kindergeld-Zuschlag zum IV-Taggeld (Art. 23bis IVG, CHF/Tag)"
    reference = "SR 831.20 Art. 23bis"

    def formula(person, period, parameters):
        hoechstbetrag = person('iv_hoechstbetrag_taggeld', period.this_year)
        anzahl_kinder = person('iv_anzahl_anspruchsberechtigte_kinder_taggeld', period)

        # 2% of max daily allowance per child
        return hoechstbetrag * 0.02 * anzahl_kinder
