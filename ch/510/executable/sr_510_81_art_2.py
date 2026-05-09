"""SR 510.81 Art. 2 - Beguenstigte

Generated from: ch/510/de/510.81.md

Beguenstigte sind PfP-Truppen sowie ihre Mitglieder und das zivile Gefolge.
Ausgenommen: Schweizer Staatsangehoerige und Personen mit Wohnsitz in der Schweiz.
Kein Anspruch fuer Einzelpersonen mit kurzfristiger Abdetachierung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_schweizer_staatsangehoeriger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person schweizerische Staatsangehoerigkeit hat"
    reference = "SR 510.81 Art. 2 Abs. 2"


class hat_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ihren Wohnsitz in der Schweiz hat"
    reference = "SR 510.81 Art. 2 Abs. 2"


class ist_einzelperson_kurze_abdetachierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Einzelperson fuer kurze Dauer in die Schweiz abdetachiert wird"
    reference = "SR 510.81 Art. 2 Abs. 3"


class ist_beguenstigter_pfp_zollbefreiung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Beguenstigte/r der Zoll- und Steuerbefreiung fuer PfP-Truppen ist"
    reference = "SR 510.81 Art. 2"

    def formula(person, period, parameters):
        ist_pfp = (
            person('ist_mitglied_pfp_truppe', period)
            + person('ist_ziviles_gefolge_pfp', period)
        ) > 0
        ausgeschlossen = (
            person('ist_schweizer_staatsangehoeriger', period)
            + person('hat_wohnsitz_schweiz', period)
            + person('ist_einzelperson_kurze_abdetachierung', period)
        ) > 0
        return ist_pfp * not_(ausgeschlossen)
