"""SR 120.4 Art. 4

Generated from: ch/120/de/120.4.md

Bedienstete des Bundes: Federal employees designated for functions in Annex 1
must undergo personnel security checks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_bediensteter_des_bundes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Bedienstete/r des Bundes ist"
    reference = "SR 120.4 Art. 4"


class funktion_nach_anhang_1(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fuer eine Funktion nach Anhang 1 vorgesehen ist"
    reference = "SR 120.4 Art. 4 Abs. 1"


class psp_pflicht_bedienstete(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Bedienstete/r einer Personensicherheitspruefung unterzogen wird"
    reference = "SR 120.4 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return person('funktion_nach_anhang_1', period)
