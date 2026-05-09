"""SR 933.011.3 Art. 1

Generated from: ch/933/de/933.011.3.md

Als technische Vorschriften zum Vollzug des Bauproduktegesetzes (BauPG)
und der BauPV gelten die in den Anhaengen 1 und 2 aufgefuehrten
Rechtsakte der Europaeischen Union.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bauprodukt_unterliegt_eu_rechtsakt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Bauprodukt einem in Anhang 1 oder 2 aufgefuehrten EU-Rechtsakt unterliegt"
    reference = "SR 933.011.3 Art. 1"


class bauprodukt_konform_technische_vorschriften(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Bauprodukt den technischen Vorschriften nach BauPG und BauPV entspricht"
    reference = "SR 933.011.3 Art. 1"

    def formula_2014(person, period, parameters):
        unterliegt = person('bauprodukt_unterliegt_eu_rechtsakt', period)
        # Konformitaet setzt voraus, dass das Produkt den EU-Rechtsakten entspricht
        return unterliegt
