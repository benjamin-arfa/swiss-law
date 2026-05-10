"""SR 151.342 Art. 3

Generated from: ch/151/de/151.342.md

Parkfelder fuer Gehbehinderte: Anzahl abhaengig von Gesamtparkfeldern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_parkfelder_personenwagen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Parkfelder fuer Personenwagen bei Haltepunkten"
    reference = "SR 151.342 Art. 3 Abs. 1"


class anzahl_parkfelder_gehbehinderte(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Erforderliche Anzahl Parkfelder fuer Gehbehinderte"
    reference = "SR 151.342 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        total = person('anzahl_parkfelder_personenwagen', period)
        # a. bis 50: 1, b. 51-150: 2, c. 151-350: 3, d. 351-750: 4, e. 751+: 5
        return (
            (total <= 50) * 1 +
            ((total >= 51) * (total <= 150)) * 2 +
            ((total >= 151) * (total <= 350)) * 3 +
            ((total >= 351) * (total <= 750)) * 4 +
            (total >= 751) * 5
        )
