"""SR 453.0 Art. 12

Generated from: ch/453/de/453.0.md
Dauerbewilligungen fuer die Einfuhr - Voraussetzungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_geschaeftssitz_zollgebiet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geschaeftssitz im Zollgebiet oder Zollausschlussgebiet"
    reference = "SR 453.0 Art. 12 Abs. 2 Bst. a"


class bietet_gewaehr_einhaltung_vorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bietet Gewaehr fuer Einhaltung der BGCITES/VCITES Vorschriften"
    reference = "SR 453.0 Art. 12 Abs. 2 Bst. b"


class dauerbewilligung_einfuhr_voraussetzungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen fuer Dauerbewilligung Einfuhr erfuellt"
    reference = "SR 453.0 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        sitz = person('hat_geschaeftssitz_zollgebiet', period)
        gewaehr = person('bietet_gewaehr_einhaltung_vorschriften', period)
        return sitz * gewaehr
