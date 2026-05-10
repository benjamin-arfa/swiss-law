"""SR 170.321 Art. 7a

Generated from: ch/170/de/170.321.md

Kostenersatz bei mutwilligem Verfahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_mutwillig_verfahren_veranlasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat mutwillig ein Verfahren nach Art. 7 veranlasst (Art. 7a VV-VG)"
    reference = "SR 170.321, Art. 7a"


class pflicht_kostenersatz_mutwilliges_verfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann verpflichtet werden, dem Bund die Kosten zu ersetzen (Art. 7a VV-VG)"
    reference = "SR 170.321, Art. 7a"

    def formula(person, period, parameters):
        return person('hat_mutwillig_verfahren_veranlasst', period)
