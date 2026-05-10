"""SR 641.811.31 Art. 5

Generated from: ch/641/de/641.811.31.md

Foreign vehicles subject to performance-based levy: applications per vehicle
and per month.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_auslaendisches_fahrzeug_leistungsabhaengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein auslaendisches Fahrzeug mit leistungsabhaengiger Abgabe handelt"
    reference = "SR 641.811.31 Art. 5"


class gesuchsperiode_auslaendisch(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesuchsperiode fuer auslaendische Fahrzeuge (je Fahrzeug und Monat)"
    reference = "SR 641.811.31 Art. 5"
    default_value = "monatlich"
