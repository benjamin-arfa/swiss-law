"""SR 142.206 Art. 8

Generated from: ch/142/de/142.206.md

Abfrage des automatisierten Berechnungssystems: Die zugangsberechtigten
Stellen koennen online abfragen, ob die oder der Drittstaatsangehoerige
die zulaessige Aufenthaltsdauer im Schengen-Raum ueberschritten hat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ees_aufenthaltsdauer_ueberschritten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die/der Drittstaatsangehoerige die zulaessige Aufenthaltsdauer im Schengen-Raum ueberschritten hat"
    reference = "SR 142.206 Art. 8 Abs. 1"


class ees_berechnungssystem_daten_kategorie_vi(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Berechnungssystem die Daten der Kategorie VI nach Anhang 2 liefert"
    reference = "SR 142.206 Art. 8 Abs. 2"

    def formula_2022_05(person, period, parameters):
        return True
