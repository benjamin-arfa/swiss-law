"""SR 141.0 Art. 20 - Materielle Voraussetzungen (erleichterte Einbuergerung)

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class integrationskriterien_art12_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Integrationskriterien nach Art. 12 Abs. 1 und 2 sind erfuellt"
    reference = "SR 141.0 Art. 20 Abs. 1"


class keine_gefaehrdung_sicherheit_art20(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person gefaehrdet die innere oder aeussere Sicherheit der Schweiz nicht"
    reference = "SR 141.0 Art. 20 Abs. 2"


class materielle_voraussetzungen_erleichterte_einbuergerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die materiellen Voraussetzungen fuer die erleichterte Einbuergerung sind erfuellt"
    reference = "SR 141.0 Art. 20"

    def formula(self, period, parameters):
        integration = self('integrationskriterien_art12_erfuellt', period)
        sicherheit = self('keine_gefaehrdung_sicherheit_art20', period)
        return integration * sicherheit
