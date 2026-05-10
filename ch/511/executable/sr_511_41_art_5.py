"""SR 511.41 Art. 5 – Reduktion

Generated from: ch/511/de/511.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class tage_militaerdienst_nach_abschluss(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl geleisteter Tage Militärdienst nach Abschluss der Ausbildung (Ablegen der Prüfung)"
    reference = "SR 511.41 Art. 5"
    default_value = 0


class reduktion_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Reduktion des Rückerstattungsbetrags in Prozent"
    reference = "SR 511.41 Art. 5"

    def formula(person, period, parameters):
        tage = person('tage_militaerdienst_nach_abschluss', period)
        # 0.5% Reduktion pro Tag, maximal 100%
        return min_(tage * 0.5, 100.0)


class rueckerstattungsbetrag_nach_reduktion(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Rückerstattungsbetrag nach Reduktion gemäss geleisteten Diensttagen (CHF)"
    reference = "SR 511.41 Art. 5"

    def formula(person, period, parameters):
        betrag = person('rueckerstattungsbetrag_ausbildungskosten', period)
        reduktion = person('reduktion_prozent', period)
        return betrag * (1.0 - reduktion / 100.0)
