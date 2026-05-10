"""SR 282.11 Art. 16 - Pruefung und provisorische Stundung

Generated from: ch/282/de/282.11.md

Partially procedural - models the supervisory authority's powers.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schuldnerin_unter_zwangsverwaltung_oder_beiratschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldnerin steht unter administrativer Zwangsverwaltung oder Beiratschaft"
    reference = "SR 282.11 Art. 16 Abs. 2"


class aufsichtsbehoerde_kann_sich_mit_feststellungen_begnuegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Aufsichtsbehoerde kann sich mit den Feststellungen der Schuldnerin begnuegen"
    reference = "SR 282.11 Art. 16 Abs. 2"

    def formula(self, period, parameters):
        return self('schuldnerin_unter_zwangsverwaltung_oder_beiratschaft', period)
