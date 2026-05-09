"""SR 210 Art. 20

Generated from: ch/de/210.md

Verwandtschaft: Der Grad der Verwandtschaft bestimmt sich nach der Zahl
der sie vermittelnden Geburten. In gerader Linie: Abstammung voneinander.
In Seitenlinie: Abstammung von gemeinsamer dritter Person.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class verwandtschaftsgrad(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Verwandtschaft (Anzahl vermittelnder Geburten)"
    reference = "SR 210 Art. 20"


class ist_verwandt_gerade_linie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Verwandtschaft in gerader Linie (Abstammung)"
    reference = "SR 210 Art. 20 Abs. 2"
