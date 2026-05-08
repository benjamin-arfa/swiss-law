"""SR 957.1 Art. 11

Generated from: ch/957/de/957.1.md

Verfügbare Bucheffekten:
- Verwahrungsstelle muss Bucheffekten verfügbar halten
- Menge mindestens gleich der Summe der Effektenguthaben
- Bei Unterbestand: unverzüglicher Erwerb erforderlich
- Verfügbar: bei Drittverwahrungsstelle gutgeschrieben, sammelverwahrte
  Wertpapiere, frei verfügbare Lieferansprüche (max. 8 Tage)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anzahl_verfuegbare_bucheffekten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl verfügbarer Bucheffekten bei der Verwahrungsstelle"
    reference = "SR 957.1 Art. 11 Abs. 1"


class summe_effektenguthaben(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Summe der Effektenguthaben aller Kontoinhaberinnen"
    reference = "SR 957.1 Art. 11 Abs. 1"


class hat_unterbestand_bucheffekten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Unterbestand an verfügbaren Bucheffekten besteht"
    reference = "SR 957.1 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        verfuegbar = person('anzahl_verfuegbare_bucheffekten', period)
        guthaben = person('summe_effektenguthaben', period)
        return verfuegbar < guthaben


class tage_fuer_lieferanspruch(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tage der frei verfügbaren Lieferansprüche"
    reference = "SR 957.1 Art. 11 Abs. 3 Bst. c"


class lieferanspruch_als_verfuegbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Lieferanspruch als verfügbar gilt (max. 8 Tage)"
    reference = "SR 957.1 Art. 11 Abs. 3 Bst. c"

    def formula(person, period, parameters):
        tage = person('tage_fuer_lieferanspruch', period)
        max_tage = parameters(period).sr_957_1.max_tage_lieferanspruch
        return tage <= max_tage
