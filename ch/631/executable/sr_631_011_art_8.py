"""SR 631.011 Art. 8

Generated from: ch/631/de/631.011.md

Voraussetzungen fuer den Grenzweidegang: Nachweis der Weideplatz-
kapazitaet und Mindestaufenthalt im Herkunftsland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class nachweis_weideplaetze_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ausreichende Weideplaetze/Futtervorraete nachgewiesen sind"
    reference = "SR 631.011 Art. 8 Abs. 1"


class aufenthalt_herkunftsland_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tage, die das Tier vor dem Grenzweidegang im Herkunftsland war"
    reference = "SR 631.011 Art. 8 Abs. 2"


class voraussetzungen_grenzweidegang_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob alle Voraussetzungen fuer den Grenzweidegang erfuellt sind"
    reference = "SR 631.011 Art. 8"

    def formula(person, period, parameters):
        weideplaetze = person('nachweis_weideplaetze_vorhanden', period)
        aufenthalt = person('aufenthalt_herkunftsland_tage', period)
        mindestaufenthalt = parameters(period).sr_631_011.mindestaufenthalt_herkunftsland_tage

        return weideplaetze * (aufenthalt >= mindestaufenthalt)
