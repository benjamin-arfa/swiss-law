"""SR 935.01 Art. 7

Generated from: ch/935/de/935.01.md

Strafbestimmungen:
- Busse bei vorsätzlicher oder fahrlässiger Dienstleistung ohne Erfüllung
  der Voraussetzungen nach Art. 5 Abs. 1
- Busse bei Verstoss gegen Meldepflicht
- Strafverfolgung ist Sache der Kantone
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_voraussetzung_art_5_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine der Voraussetzungen nach Art. 5 Abs. 1 erfüllt ist"
    reference = "SR 935.01 Art. 5 Abs. 1"


class erbringt_dienstleistung_ohne_berechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Dienstleistungen ohne Erfüllung der Voraussetzungen erbracht werden"
    reference = "SR 935.01 Art. 7 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        unterliegt = person('unterliegt_bgmd', period)
        berechtigt = person('hat_voraussetzung_art_5_erfuellt', period)
        return unterliegt * (1 - berechtigt)


class strafbar_nach_bgmd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine strafbare Handlung nach BGMD Art. 7 vorliegt"
    reference = "SR 935.01 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        ohne_berechtigung = person('erbringt_dienstleistung_ohne_berechtigung', period)
        meldepflicht = 1 - person('meldepflicht_erfuellt', period)
        return np.maximum(ohne_berechtigung, meldepflicht)
