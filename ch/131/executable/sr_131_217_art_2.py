"""SR 131.217 Art. 2

Generated from: ch/131/de/131.217.md

Geltung der Grundrechte: Grundrechte beschränken die Staatsgewalt.
Einschränkungen nur im Rahmen der Verfassung und aufgrund des Gesetzes.
Kein Eingriff darf weiter gehen als ein zulässiger Zweck und ein
überwiegendes öffentliches Interesse es erfordern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class grundrecht_einschraenkung_gesetzliche_grundlage_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Grundrechtseinschränkung eine gesetzliche Grundlage hat"
    reference = "SR 131.217 Art. 2 Abs. 3"


class grundrecht_einschraenkung_zulaessiger_zweck_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Grundrechtseinschränkung einen zulässigen Zweck verfolgt"
    reference = "SR 131.217 Art. 2 Abs. 4"


class grundrecht_einschraenkung_oeffentliches_interesse_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein überwiegendes öffentliches Interesse an der Einschränkung besteht"
    reference = "SR 131.217 Art. 2 Abs. 4"


class grundrecht_einschraenkung_ernste_gefahr_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Fall ernster, unmittelbarer und offensichtlicher Gefahr vorliegt"
    reference = "SR 131.217 Art. 2 Abs. 3"


class grundrecht_einschraenkung_zulaessig_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Grundrechtseinschränkung im Kanton Glarus zulässig ist"
    reference = "SR 131.217 Art. 2 Abs. 3-4"

    def formula(person, period, parameters):
        gesetzlich = person('grundrecht_einschraenkung_gesetzliche_grundlage_gl', period)
        zweck = person('grundrecht_einschraenkung_zulaessiger_zweck_gl', period)
        interesse = person('grundrecht_einschraenkung_oeffentliches_interesse_gl', period)
        gefahr = person('grundrecht_einschraenkung_ernste_gefahr_gl', period)
        # Gesetzliche Grundlage erforderlich ODER Fall ernster Gefahr
        # UND zulässiger Zweck UND überwiegendes öffentliches Interesse
        return (gesetzlich + gefahr > 0) * zweck * interesse
