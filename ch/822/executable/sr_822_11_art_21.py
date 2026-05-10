"""SR 822.11 Art. 21 - Freier Halbtag

Generated from: ch/de/822/822.11.md

If weekly working time is distributed over more than 5 days,
employees must be given one half-day off per week,
except in weeks containing a public holiday.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arbeitstage_pro_woche(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Arbeitstage pro Woche"
    reference = "SR 822.11 Art. 21 Abs. 1"


class woche_enthaelt_arbeitsfreien_tag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Woche einen arbeitsfreien Tag (Feiertag) enthaelt"
    reference = "SR 822.11 Art. 21 Abs. 1"


class anspruch_freier_halbtag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Anspruch auf einen freien Halbtag pro Woche besteht"
    reference = "SR 822.11 Art. 21 Abs. 1"

    def formula(person, period, parameters):
        tage = person('arbeitstage_pro_woche', period)
        feiertag_woche = person('woche_enthaelt_arbeitsfreien_tag', period)
        return (tage > 5) * (1 - feiertag_woche)
