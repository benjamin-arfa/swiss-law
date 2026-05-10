"""SR 704.1 Art. 7

Generated from: ch/704/de/704.1.md

Empfaenger von Bundesbeitraegen: Federal contributions to private non-profit
organizations dedicated to promoting foot and hiking path networks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fachorganisation_gemeinnuetzig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation auf gemeinnuetziger Grundlage taetig ist"
    reference = "SR 704.1 Art. 7 Abs. 1"


class fachorganisation_ueberwiegend_fww_foerderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ueberwiegend der Foerderung der Fuss- und Wanderwegnetze dient"
    reference = "SR 704.1 Art. 7 Abs. 1"


class fachorganisation_bundesbeitragsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die private Fachorganisation bundesbeitragsberechtigt ist"
    reference = "SR 704.1 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('fachorganisation_gemeinnuetzig', period) *
            person('fachorganisation_ueberwiegend_fww_foerderung', period)
        )
