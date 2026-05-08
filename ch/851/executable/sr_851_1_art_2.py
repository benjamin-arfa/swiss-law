"""SR 851.1 Art. 2

Generated from: ch/851/de/851.1.md

Art. 2: Beduerftigkeitsbegriff
- Abs. 1: Beduerftigkeit liegt vor, wenn eine Person fuer ihren Lebensunterhalt
  nicht hinreichend oder nicht rechtzeitig aus eigenen Mitteln aufkommen kann.
- Abs. 2: Die Beduerftigkeitsbemessung richtet sich nach den am Unterstuetzungsort
  geltenden Vorschriften und Grundsaetzen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zug_eigene_mittel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Eigene Mittel fuer den Lebensunterhalt (CHF/Monat)"
    reference = "SR 851.1 Art. 2 Abs. 1"


class zug_lebensunterhalt_bedarf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Bedarf fuer den Lebensunterhalt (CHF/Monat)"
    reference = "SR 851.1 Art. 2 Abs. 1"


class zug_beduerftigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beduerftig im Sinne des ZUG (eigene Mittel genuegen nicht fuer Lebensunterhalt)"
    reference = "SR 851.1 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        eigene_mittel = person('zug_eigene_mittel', period)
        bedarf = person('zug_lebensunterhalt_bedarf', period)
        return eigene_mittel < bedarf
