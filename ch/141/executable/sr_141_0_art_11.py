"""SR 141.0 Art. 11 - Materielle Voraussetzungen

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class erfolgreich_integriert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist erfolgreich integriert"
    reference = "SR 141.0 Art. 11 lit. a"


class mit_schweizerischen_lebensverhaeltnissen_vertraut(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist mit den schweizerischen Lebensverhaeltnissen vertraut"
    reference = "SR 141.0 Art. 11 lit. b"


class keine_gefaehrdung_sicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person stellt keine Gefaehrdung der inneren oder aeusseren Sicherheit der Schweiz dar"
    reference = "SR 141.0 Art. 11 lit. c"


# Computed variables

class materielle_voraussetzungen_einbuergerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die materiellen Voraussetzungen fuer die Einbuergerungsbewilligung des Bundes sind erfuellt"
    reference = "SR 141.0 Art. 11"

    def formula(self, period, parameters):
        integriert = self('erfolgreich_integriert', period)
        vertraut = self('mit_schweizerischen_lebensverhaeltnissen_vertraut', period)
        sicher = self('keine_gefaehrdung_sicherheit', period)
        return integriert * vertraut * sicher
