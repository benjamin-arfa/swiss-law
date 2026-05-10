"""SR 823.113 Art. 2

Generated from: ch/823/de/823.113.md

Einschreibgebühr für Stellensuchende in der Arbeitsvermittlung:
- Höchstens 45 CHF pro Vermittlungsauftrag (Inland und Ausland)
- Darf nur einmal pro Vermittlungsauftrag erhoben werden
- Erfolgloser Auftrag erlischt nach 6 Monaten
- Bei Zusammenarbeit mehrerer Vermittler: keine Kumulierung
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einschreibgebuehr_arbeitsvermittlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Einschreibgebühr für Stellensuchende (max. 45 CHF pro Vermittlungsauftrag)"
    reference = "SR 823.113 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        gebuehr = person('geplante_einschreibgebuehr', period)
        max_gebuehr = parameters(period).sr_823_113.einschreibgebuehr_max
        return np.minimum(gebuehr, max_gebuehr)


class geplante_einschreibgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vom Vermittler geplante Einschreibgebühr vor gesetzlicher Begrenzung"
    reference = "SR 823.113 Art. 2"
