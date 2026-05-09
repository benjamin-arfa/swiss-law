"""SR 210 Art. 23

Generated from: ch/de/210.md

Wohnsitz: Der Wohnsitz einer Person befindet sich an dem Orte, wo sie sich
mit der Absicht dauernden Verbleibens aufhaelt. Aufenthalt zum Zweck der
Ausbildung oder Unterbringung in Einrichtungen begruendet keinen Wohnsitz.
Niemand kann an mehreren Orten zugleich Wohnsitz haben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person einen Wohnsitz in der Schweiz hat"
    reference = "SR 210 Art. 23"


class ist_aufenthalt_ausbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Aufenthalt zum Zweck der Ausbildung (begruendet keinen Wohnsitz)"
    reference = "SR 210 Art. 23 Abs. 1"


class ist_aufenthalt_einrichtung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unterbringung in Erziehungs-/Pflegeeinrichtung/Spital/Strafanstalt"
    reference = "SR 210 Art. 23 Abs. 1"


class hat_wohnsitz_begruendend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Aufenthalt wohnsitzbegruendend ist (dauerndes Verbleiben)"
    reference = "SR 210 Art. 23"

    def formula(person, period, parameters):
        # Wohnsitz = Absicht dauernden Verbleibens
        # MINUS Ausnahmen (Ausbildung, Einrichtung)
        hat_absicht_dauerndes_verbleiben = person('hat_absicht_dauerndes_verbleiben', period)
        ist_ausbildung = person('ist_aufenthalt_ausbildung', period)
        ist_einrichtung = person('ist_aufenthalt_einrichtung', period)
        return hat_absicht_dauerndes_verbleiben * not_(ist_ausbildung) * not_(ist_einrichtung)


class hat_absicht_dauerndes_verbleiben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person die Absicht dauernden Verbleibens hat"
    reference = "SR 210 Art. 23 Abs. 1"
