"""SR 702.1 Art. 2

Generated from: ch/702/de/702.1.md

Aufgaben und Kompetenzen des Bundes: The ARE determines by 31 March each year
whether a municipality's second home share exceeds 20%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gemeinde_gesamtzahl_wohnungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtzahl der Wohnungen in der Gemeinde"
    reference = "SR 702.1 Art. 2 Abs. 4"


class gemeinde_anzahl_erstwohnungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Erstwohnungen in der Gemeinde"
    reference = "SR 702.1 Art. 2 Abs. 4"


class gemeinde_erstwohnungsanteil_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erstwohnungsanteil der Gemeinde in Prozent"
    reference = "SR 702.1 Art. 2 Abs. 4"

    def formula(person, period, parameters):
        gesamt = person('gemeinde_gesamtzahl_wohnungen', period)
        erst = person('gemeinde_anzahl_erstwohnungen', period)
        return where(gesamt > 0, erst / gesamt * 100, 0)


class gemeinde_zweitwohnungsanteil_ueber_20_prozent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zweitwohnungsanteil der Gemeinde mehr als 20 Prozent betraegt"
    reference = "SR 702.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        erstwohnungsanteil = person('gemeinde_erstwohnungsanteil_prozent', period)
        return erstwohnungsanteil < 80  # Zweitwohnungsanteil > 20% iff Erstwohnungsanteil < 80%


class zweitwohnungsanteil_feststellung_frist_tag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Feststellung des Zweitwohnungsanteils (Tag im Maerz)"
    reference = "SR 702.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return 31  # 31. Maerz
