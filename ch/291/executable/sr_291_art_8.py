"""SR 291 Art. 8

Generated from: ch/291/de/291.md

Widerklage: Das Gericht, bei dem die Hauptklage haengig ist, beurteilt
auch die Widerklage, sofern zwischen Haupt- und Widerklage ein sachlicher
Zusammenhang besteht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hauptklage_haengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Hauptklage bei einem schweizerischen Gericht haengig ist"
    reference = "SR 291 Art. 8"


class sachlicher_zusammenhang_widerklage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob zwischen Haupt- und Widerklage ein sachlicher Zusammenhang besteht"
    reference = "SR 291 Art. 8"


class widerklage_am_hauptklage_gericht_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Widerklage am Gericht der Hauptklage beurteilt wird"
    reference = "SR 291 Art. 8"

    def formula(person, period, parameters):
        hauptklage = person('hauptklage_haengig', period)
        zusammenhang = person('sachlicher_zusammenhang_widerklage', period)
        return hauptklage * zusammenhang
