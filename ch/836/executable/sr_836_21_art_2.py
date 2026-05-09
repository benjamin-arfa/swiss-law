"""SR 836.21 Art. 2 - Birth allowance (Geburtszulage)

Art. 2: Entitlement to a birth allowance exists when the cantonal family
allowance scheme provides for one. The allowance is paid if (a) there is
an entitlement to family allowances under FamZG, and (b) the mother has had
domicile or habitual residence in Switzerland for 9 months before birth.
If multiple persons are entitled, the one with primary entitlement receives it;
if the secondary person's amount is higher, they receive the difference.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class kanton_sieht_geburtszulage_vor(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Canton provides for a birth allowance (Art. 2 par. 1 FamZV)"
    default_value = False


class anspruch_familienzulagen_famzg(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to family allowances under FamZG (Art. 2 par. 3 let. a FamZV)"
    default_value = False


class mutter_wohnsitz_schweiz_9_monate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Mother had domicile/habitual residence in CH for 9 months before birth (Art. 2 par. 3 let. b FamZV)"
    default_value = False


class geburt_vorzeitig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Birth occurred prematurely (Art. 2 par. 3 let. b FamZV)"
    default_value = False


class anspruch_geburtszulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to birth allowance (Art. 2 FamZV)"

    def formula(person, period, parameters):
        kanton = person("kanton_sieht_geburtszulage_vor", period)
        famzg = person("anspruch_familienzulagen_famzg", period)
        wohnsitz = person("mutter_wohnsitz_schweiz_9_monate", period)
        return kanton * famzg * wohnsitz


class geburtszulage_erstanspruch(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Birth allowance amount of primary entitled person (Art. 2 par. 4 FamZV)"
    default_value = 0


class geburtszulage_zweitanspruch(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Birth allowance amount of secondary entitled person (Art. 2 par. 4 FamZV)"
    default_value = 0


class geburtszulage_differenz(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Difference payable to secondary entitled person if their amount is higher (Art. 2 par. 4 FamZV)"

    def formula(person, period, parameters):
        erst = person("geburtszulage_erstanspruch", period)
        zweit = person("geburtszulage_zweitanspruch", period)
        return max_(0, zweit - erst)
