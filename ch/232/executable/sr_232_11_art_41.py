"""SR 232.11 Art. 41

Generated from: ch/232/de/232.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class monate_seit_kenntnis_fristversaeumnis(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Monate seit Kenntnis der Fristversäumnis"
    reference = "SR 232.11 Art. 41 Abs. 2"


class monate_seit_ablauf_versaeumter_frist(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Monate seit Ablauf der versäumten Frist"
    reference = "SR 232.11 Art. 41 Abs. 2"


class unterbliebene_handlung_nachgeholt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die unterbliebene Handlung wurde vollständig nachgeholt"
    reference = "SR 232.11 Art. 41 Abs. 2"


class gebuehren_fuer_weiterbehandlung_bezahlt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Gebühren für die Weiterbehandlung wurden bezahlt"
    reference = "SR 232.11 Art. 41 Abs. 2"


class weiterbehandlung_ausgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Weiterbehandlung ist nach Art. 41 Abs. 4 ausgeschlossen"
    reference = "SR 232.11 Art. 41 Abs. 4"


class weiterbehandlung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Weiterbehandlung bei Fristversäumnis ist möglich"
    reference = "SR 232.11 Art. 41"

    def formula(person, period, parameters):
        monate_kenntnis = person('monate_seit_kenntnis_fristversaeumnis', period)
        monate_ablauf = person('monate_seit_ablauf_versaeumter_frist', period)
        nachgeholt = person('unterbliebene_handlung_nachgeholt', period)
        bezahlt = person('gebuehren_fuer_weiterbehandlung_bezahlt', period)
        ausgeschlossen = person('weiterbehandlung_ausgeschlossen', period)
        # Antrag innerhalb von 2 Monaten seit Kenntnis, max 6 Monate seit Ablauf
        frist_ok = (monate_kenntnis <= 2) * (monate_ablauf <= 6)
        return frist_ok * nachgeholt * bezahlt * not_(ausgeschlossen)
