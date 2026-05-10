"""SR 281.1 Art. 17

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beschwerde_wegen_gesetzesverletzung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beschwerde wegen Gesetzesverletzung oder Unangemessenheit"
    reference = "SR 281.1 Art. 17 Abs. 1"


class tage_seit_kenntnis_verfuegung(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Tage seit Kenntnis der angefochtenen Verfügung"
    reference = "SR 281.1 Art. 17 Abs. 2"


class beschwerde_wegen_rechtsverweigerung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beschwerde wegen Rechtsverweigerung oder Rechtsverzögerung"
    reference = "SR 281.1 Art. 17 Abs. 3"


class beschwerdefrist_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beschwerdefrist von 10 Tagen ist eingehalten"
    reference = "SR 281.1 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        tage = person('tage_seit_kenntnis_verfuegung', period)
        rechtsverweigerung = person('beschwerde_wegen_rechtsverweigerung', period)
        # 10 Tage Frist, oder jederzeit bei Rechtsverweigerung
        return (tage <= 10) + rechtsverweigerung
