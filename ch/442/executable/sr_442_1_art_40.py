"""SR 442.1 Art. 40

Generated from: ch/442/de/442.1.md

Finanzierung Pro Helvetia: Unantastbares Stiftungsvermoegen von 100'000 CHF.
Jaehrliche Beitraege des Bundes. Zweckfreie Zuwendungen Dritter werden zum
Stiftungsvermoegen geschlagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stiftungsvermoegen_pro_helvetia(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Unantastbares Stiftungsvermoegen Pro Helvetia (CHF)"
    reference = "SR 442.1 Art. 40 Abs. 1"
    default_value = 100000


class zuwendungen_dritter_ohne_zweckbestimmung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zuwendungen Dritter ohne besondere Zweckbestimmung (CHF)"
    reference = "SR 442.1 Art. 40 Abs. 3"


class stiftungsvermoegen_gesamt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtes Stiftungsvermoegen inkl. Zuwendungen Dritter"
    reference = "SR 442.1 Art. 40"

    def formula(person, period, parameters):
        basis = person('stiftungsvermoegen_pro_helvetia', period)
        zuwendungen = person('zuwendungen_dritter_ohne_zweckbestimmung', period)
        return basis + zuwendungen
