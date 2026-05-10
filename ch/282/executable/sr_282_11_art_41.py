"""SR 282.11 Art. 41 - Betreibungsstopp waehrend Beiratschaft

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beiratschaft_besteht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Beiratschaft besteht"
    reference = "SR 282.11 Art. 41 Abs. 1"


class verpflichtung_vor_beiratschaft_eingegangen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung wurde vor Anordnung der Beiratschaft eingegangen"
    reference = "SR 282.11 Art. 41 Abs. 1"


class betreibung_gesperrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betreibungen koennen nicht angehoben oder fortgesetzt werden"
    reference = "SR 282.11 Art. 41 Abs. 1"

    def formula(self, period, parameters):
        beiratschaft = self('beiratschaft_besteht', period)
        vor_beiratschaft = self('verpflichtung_vor_beiratschaft_eingegangen', period)
        return beiratschaft * vor_beiratschaft


class verjaehrung_gehemmt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Lauf der Verjaerungs- und Verwirkungsfristen ist gehemmt"
    reference = "SR 282.11 Art. 41 Abs. 2"

    def formula(self, period, parameters):
        return self('betreibung_gesperrt', period)
