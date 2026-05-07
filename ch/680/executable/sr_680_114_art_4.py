"""SR 680.114 Art. 4

Generated from: ch/680/de/680.114.md

Abzug der Fehlmengen und Verluste: Shortages and losses must be deducted
from the taxable quantity of spirits.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class branntwein_bruttomenge_liter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttomenge gebrannter Wasser in Litern (vor Abzug)"
    reference = "SR 680.114 Art. 4"


class branntwein_fehlmengen_liter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anerkannte Fehlmengen in Litern"
    reference = "SR 680.114 Art. 4"


class branntwein_verluste_liter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anerkannte Verluste in Litern"
    reference = "SR 680.114 Art. 4"


class branntwein_steuerpflichtige_menge_liter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fuer die Besteuerung massgebende Menge gebrannter Wasser in Litern"
    reference = "SR 680.114 Art. 4"

    def formula(person, period, parameters):
        brutto = person('branntwein_bruttomenge_liter', period)
        fehlmengen = person('branntwein_fehlmengen_liter', period)
        verluste = person('branntwein_verluste_liter', period)
        return max_(brutto - fehlmengen - verluste, 0)
