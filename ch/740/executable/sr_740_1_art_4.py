"""SR 740.1 Art. 4 - Evaluation und Steuerung des Verlagerungsprozesses

Generated from: ch/740/de/740.1.md

Der Bundesrat ueberprüft regelmaessig die Wirksamkeit und erstattet
der Bundesversammlung alle zwei Jahre einen Bericht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class massnahmen_verhaeltnismaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verlagerungsmassnahmen sind verhaeltnismaessig"
    reference = "SR 740.1 Art. 4 Abs. 3"


class massnahmen_laengerfristig_marktkonform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verlagerungsmassnahmen sind laengerfristig marktkonform"
    reference = "SR 740.1 Art. 4 Abs. 3"


class massnahmen_nichtdiskriminierend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verlagerungsmassnahmen sind nichtdiskriminierend"
    reference = "SR 740.1 Art. 4 Abs. 3"


class massnahmen_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verlagerungsmassnahmen erfuellen alle Anforderungen nach Art. 4 Abs. 3"
    reference = "SR 740.1 Art. 4 Abs. 3"

    def formula(self, period, parameters):
        verhaeltnismaessig = self('massnahmen_verhaeltnismaessig', period)
        marktkonform = self('massnahmen_laengerfristig_marktkonform', period)
        nichtdiskriminierend = self('massnahmen_nichtdiskriminierend', period)
        return verhaeltnismaessig * marktkonform * nichtdiskriminierend
