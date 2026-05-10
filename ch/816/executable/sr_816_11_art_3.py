"""SR 816.11 Art. 3

Generated from: ch/816/de/816.11.md

Dauer der Zugriffsrechte: Einzelpersonen unbefristet bis Entzug,
Gruppen muessen befristet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_zugriffsrecht_fuer_gruppe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Zugriffsrecht fuer eine Gruppe von Gesundheitsfachpersonen erteilt wurde"
    reference = "SR 816.11 Art. 3 Abs. 2"


class hat_patient_zugriffsrecht_entzogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin/der Patient das Zugriffsrecht entzogen hat"
    reference = "SR 816.11 Art. 3 Abs. 1"


class ist_befristung_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Befristung des Gruppenrechts abgelaufen ist"
    reference = "SR 816.11 Art. 3 Abs. 2"


class zugriffsrecht_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Zugriffsrecht aktuell gueltig ist"
    reference = "SR 816.11 Art. 3"

    def formula(person, period, parameters):
        entzogen = person('hat_patient_zugriffsrecht_entzogen', period)
        ist_gruppe = person('ist_zugriffsrecht_fuer_gruppe', period)
        befristung_abgelaufen = person('ist_befristung_abgelaufen', period)
        # Einzelperson: gueltig bis Entzug; Gruppe: gueltig bis Entzug oder Ablauf
        return (1 - entzogen) * (1 - ist_gruppe * befristung_abgelaufen)
