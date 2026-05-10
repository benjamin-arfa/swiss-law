"""SR 251 Art. 52

Generated from: ch/de/251.md

Administrative sanction for failure to provide information or
documents: fine up to CHF 100,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auskunftspflicht_nicht_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Auskunftspflicht oder Urkundenvorlagepflicht nicht oder nicht richtig erfuellt wird"
    reference = "SR 251 Art. 52"


class verwaltungssanktion_art52_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Belastungsbetrag nach Art. 52 (CHF)"
    reference = "SR 251 Art. 52"

    def formula(person, period, parameters):
        return person('auskunftspflicht_nicht_erfuellt', period) * 100000.0
