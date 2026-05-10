"""SR 195.1 Art. 24

Generated from: ch/195/de/195.1.md

Subsidiaritaet: Sozialhilfe nur wenn Lebensunterhalt nicht aus eigenen
Kraeften, privaten Beitraegen oder Hilfeleistungen des Empfangsstaates
bestritten werden kann.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kann_lebensunterhalt_selbst_bestreiten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ihren Lebensunterhalt aus eigenen Kraeften und Mitteln bestreiten kann"
    reference = "SR 195.1 Art. 24"


class erhaelt_beitraege_privater_seite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Beitraege von privater Seite erhaelt"
    reference = "SR 195.1 Art. 24"


class erhaelt_hilfeleistungen_empfangsstaat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Hilfeleistungen des Empfangsstaates erhaelt"
    reference = "SR 195.1 Art. 24"


class anspruch_auf_sozialhilfe_subsidiaritaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Subsidiaritaetsbedingung fuer Sozialhilfe erfuellt ist"
    reference = "SR 195.1 Art. 24"

    def formula(person, period, parameters):
        selbst = person('kann_lebensunterhalt_selbst_bestreiten', period)
        privat = person('erhaelt_beitraege_privater_seite', period)
        staat = person('erhaelt_hilfeleistungen_empfangsstaat', period)
        # Sozialhilfe nur wenn keine andere Quelle ausreichend
        return (1 - selbst) * (1 - privat) * (1 - staat)
