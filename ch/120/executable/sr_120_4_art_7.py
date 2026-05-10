"""SR 120.4 Art. 7

Generated from: ch/120/de/120.4.md

Angestellte der Kantone: Cantonal employees undergo PSP on request of the
competent cantonal authority when designated for BWIS functions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_angestellter_des_kantons(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Angestellte/r eines Kantons ist"
    reference = "SR 120.4 Art. 7"


class funktion_mit_bwis_mitwirkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Funktion unmittelbare Mitwirkung bei BWIS-Aufgaben umfasst"
    reference = "SR 120.4 Art. 7"


class psp_pflicht_kantonsangestellte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob kantonale Angestellte einer PSP unterzogen werden"
    reference = "SR 120.4 Art. 7"

    def formula(person, period, parameters):
        return (
            person('ist_angestellter_des_kantons', period) *
            person('funktion_mit_bwis_mitwirkung', period)
        )
