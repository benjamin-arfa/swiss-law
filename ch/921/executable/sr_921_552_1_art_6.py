"""SR 921.552.1 Art. 6

Generated from: ch/921/de/921.552.1.md

Amtliches Zeugnis fuer die Einfuhr: Importeur muss amtliches Zeugnis
nach Muster in Anhang 5 vorlegen, oder ein gleichwertiges Zeugnis.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vermehrungsgut_import_amtliches_zeugnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein amtliches Zeugnis fuer die Einfuhr vorliegt"
    reference = "SR 921.552.1 Art. 6 Abs. 1"


class vermehrungsgut_import_gleichwertiges_zeugnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein gleichwertiges amtliches Zeugnis fuer die Einfuhr vorliegt"
    reference = "SR 921.552.1 Art. 6 Abs. 2"


class vermehrungsgut_import_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einfuhr von forstlichem Vermehrungsgut zulaessig ist"
    reference = "SR 921.552.1 Art. 6"

    def formula(person, period, parameters):
        amtlich = person('vermehrungsgut_import_amtliches_zeugnis', period)
        gleichwertig = person('vermehrungsgut_import_gleichwertiges_zeugnis', period)
        return amtlich + gleichwertig
