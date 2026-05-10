"""SR 282.11 Art. 4 - Betreibungsamt und Beschwerde

Generated from: ch/282/de/282.11.md

Partially procedural - models the complaint deadline.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beschwerdefrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Beschwerde gegen Verfuegungen des Betreibungsamtes in Tagen"
    reference = "SR 282.11 Art. 4 Abs. 2"

    def formula(self, period, parameters):
        return 10


class beschwerde_wegen_rechtsverweigerung_jederzeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschwerde wegen Rechtsverweigerung und Rechtsverzoegerung kann jederzeit gefuehrt werden"
    reference = "SR 282.11 Art. 4 Abs. 3"

    def formula(self, period, parameters):
        return 1
