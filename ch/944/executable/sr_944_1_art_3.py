"""SR 944.1 Art. 3

Generated from: ch/944/de/944.1.md

Abstimmungen: Quorum and voting rules for the Federal Consumer Affairs
Commission. Quorum: at least half of members present. Simple majority.
Chair has casting vote on ties.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ekk_anzahl_mitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Mitglieder der Eidgenoessischen Kommission fuer Konsumentenfragen"
    reference = "SR 944.1 Art. 3 Abs. 1"


class ekk_anzahl_anwesend(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl anwesende Mitglieder"
    reference = "SR 944.1 Art. 3 Abs. 1"
    default_value = 0


class ekk_ist_beschlussfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission beschlussfaehig ist (mind. Haelfte anwesend)"
    reference = "SR 944.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        mitglieder = person('ekk_anzahl_mitglieder', period)
        anwesend = person('ekk_anzahl_anwesend', period)
        return anwesend >= (mitglieder / 2)


class ekk_einberufungsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Frist fuer Einberufung auf Verlangen von 5 Mitgliedern (Tage)"
    reference = "SR 944.1 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 20
