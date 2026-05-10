"""SR 313.32 Art. 14

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class akteneinsicht_gebuehr(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Akteneinsicht in erledigte Sache (15 CHF)"
    reference = "SR 313.32 Art. 14 Abs. 1"
    default_value = 15.0


class amtliche_nachforschung_gebuehr_pro_halbe_stunde(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer amtliche Nachforschungen pro angefangene halbe Stunde (30 CHF)"
    reference = "SR 313.32 Art. 14 Abs. 2"
    default_value = 30.0


class nachforschung_halbe_stunden(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl angefangene halbe Stunden fuer Nachforschungen"
    reference = "SR 313.32 Art. 14"


class nachforschung_gebuehr_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Totale Gebuehr fuer amtliche Nachforschungen"
    reference = "SR 313.32 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        halbe_stunden = person('nachforschung_halbe_stunden', period)
        return halbe_stunden * 30.0
