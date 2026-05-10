"""SR 141.0 Art. 36 - Nichtigerklaerung

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class einbuergerung_durch_falsche_angaben_erschlichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Einbuergerung wurde durch falsche Angaben oder Verheimlichung erheblicher Tatsachen erschlichen"
    reference = "SR 141.0 Art. 36 Abs. 1"


class jahre_seit_erwerb_buergerrecht(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit Erwerb des Schweizer Buergerrechts"
    reference = "SR 141.0 Art. 36 Abs. 2"


class jahre_seit_kenntnis_sachverhalt(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit das SEM vom rechtserheblichen Sachverhalt Kenntnis erhalten hat"
    reference = "SR 141.0 Art. 36 Abs. 2"


# Computed variables

class nichtigerklaerung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Einbuergerung kann nichtig erklaert werden"
    reference = "SR 141.0 Art. 36"

    def formula(self, period, parameters):
        erschlichen = self('einbuergerung_durch_falsche_angaben_erschlichen', period)
        seit_erwerb = self('jahre_seit_erwerb_buergerrecht', period)
        seit_kenntnis = self('jahre_seit_kenntnis_sachverhalt', period)

        # Abs. 2: Innerhalb von 2 Jahren seit Kenntnis, spaetestens 8 Jahre seit Erwerb
        frist_ok = (seit_kenntnis <= 2) * (seit_erwerb <= 8)

        return erschlichen * frist_ok
