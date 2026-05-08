"""SR 857.5 Art. 2

Generated from: ch/857/de/857.5.md

Amts- und Berufsgeheimnis (Official and professional secrecy).
Staff of counseling centers are subject to secrecy obligations under
Art. 320 or 321 StGB. Art. 321 Ziff. 3 StGB (duty to testify) does NOT
apply, except criminal procedure obligations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class schwangerschaftsberatung_geheimhaltungspflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Untersteht die Person der Geheimhaltungspflicht als Mitarbeiter/in einer Beratungsstelle?"
    reference = "SR 857.5 Art. 2 Abs. 1"

    def formula_1984(person, period, parameters):
        return person('schwangerschaftsberatung_mitarbeiter', period)


class schwangerschaftsberatung_geheimhaltung_entfaellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Entfällt die Geheimhaltungspflicht wegen unwahren Angaben oder betrügerischen Machenschaften?"
    reference = "SR 857.5 Art. 2 Abs. 2"

    def formula_1984(person, period, parameters):
        return person('schwangerschaftsberatung_betrug_festgestellt', period)


class schwangerschaftsberatung_mitarbeiter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist Mitarbeiter/in einer Schwangerschaftsberatungsstelle"
    reference = "SR 857.5 Art. 2"


class schwangerschaftsberatung_betrug_festgestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hat jemand finanzielle Leistungen durch unwahre Angaben oder Betrug erwirkt?"
    reference = "SR 857.5 Art. 2 Abs. 2"
