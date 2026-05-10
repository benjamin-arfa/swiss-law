"""SR 512.271.1 Art. 6 – Fliegermedizinische Tauglichkeitsuntersuchung

Generated from: ch/512/de/512.271.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 512.271.1 Art. 6"
    default_value = 0


class ist_pilot(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Militärpilot/in oder Angehörige/r des Fallschirmsprungdienstes"
    reference = "SR 512.271.1 Art. 6 Abs. 1 lit. a"
    default_value = False


class ist_bordoperateur_oder_drohnenoperateur(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Bordoperateur/in oder Drohnenoperateur/in"
    reference = "SR 512.271.1 Art. 6 Abs. 1 lit. b"
    default_value = False


class gueltigkeitsdauer_tauglichkeitsattest_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gültigkeitsdauer des ärztlichen Tauglichkeitsattests in Monaten"
    reference = "SR 512.271.1 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        alter_val = person('alter', period)
        ist_pilot_val = person('ist_pilot', period)
        ist_bord = person('ist_bordoperateur_oder_drohnenoperateur', period)

        # Art. 6 Abs. 1 lit. a: Piloten/Fallschirmspringer:
        #   bis 40. Altersjahr: 12 Monate, ab 41.: 6 Monate
        pilot_dauer = where(alter_val <= 40, 12, 6)

        # Art. 6 Abs. 1 lit. b: Bordoperateure/Drohnenoperateure: 12 Monate
        bord_dauer = 12

        return where(ist_pilot_val, pilot_dauer,
               where(ist_bord, bord_dauer, 0))
