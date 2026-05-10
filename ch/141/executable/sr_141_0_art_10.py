"""SR 141.0 Art. 10 - Voraussetzungen bei eingetragener Partnerschaft

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class eingetragene_partnerschaft_mit_schweizer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist eine eingetragene Partnerschaft mit einer Schweizer Buergerin oder einem Schweizer Buerger eingegangen"
    reference = "SR 141.0 Art. 10 Abs. 1"


class aufenthalt_schweiz_gesamt_jahre_art10(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtaufenthalt in der Schweiz in Jahren (fuer Art. 10)"
    reference = "SR 141.0 Art. 10 Abs. 1 lit. a"


class aufenthalt_unmittelbar_vor_gesuch_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthalt unmittelbar vor Gesuchstellung in Jahren"
    reference = "SR 141.0 Art. 10 Abs. 1 lit. a"


class dauer_eingetragene_partnerschaft_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer des Zusammenlebens in eingetragener Partnerschaft in Jahren"
    reference = "SR 141.0 Art. 10 Abs. 1 lit. b"


# Computed variables

class voraussetzungen_eingetragene_partnerschaft_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Voraussetzungen bei eingetragener Partnerschaft fuer die ordentliche Einbuergerung sind erfuellt"
    reference = "SR 141.0 Art. 10"

    def formula(self, period, parameters):
        partnerschaft = self('eingetragene_partnerschaft_mit_schweizer', period)
        aufenthalt = self('aufenthalt_schweiz_gesamt_jahre_art10', period)
        unmittelbar = self('aufenthalt_unmittelbar_vor_gesuch_jahre', period)
        dauer = self('dauer_eingetragene_partnerschaft_jahre', period)

        # Abs. 1 lit. a: 5 Jahre insgesamt, davon 1 unmittelbar vor Gesuch
        # Abs. 1 lit. b: seit 3 Jahren in eingetragener Partnerschaft
        return partnerschaft * (aufenthalt >= 5) * (unmittelbar >= 1) * (dauer >= 3)
