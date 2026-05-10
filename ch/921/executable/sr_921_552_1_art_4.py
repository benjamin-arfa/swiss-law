"""SR 921.552.1 Art. 4

Generated from: ch/921/de/921.552.1.md

Verwendung von Vermehrungsgut:
Abs. 1: Fuer forstliche Zwecke nur mit nachgewiesener Herkunft (Art. 3)
        und Anerkennung als standortgerecht durch kantonale Forstbehoerde.
Abs. 2: Anderes Vermehrungsgut nur fuer wissenschaftliche Versuche oder Zuechtung.
Abs. 3: Eigener Wald: Eigenbedarf am Ort der Herkunft erlaubt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermehrungsgut_standortgerecht_anerkannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vermehrungsgut als standortgerecht anerkannt ist"
    reference = "SR 921.552.1 Art. 4 Abs. 1"


class vermehrungsgut_eigener_wald(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vermehrungsgut im eigenen Wald gesammelt wurde"
    reference = "SR 921.552.1 Art. 4 Abs. 3"


class vermehrungsgut_verwendung_fuer_forschung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Verwendung fuer wissenschaftliche Versuche oder Zuechtung"
    reference = "SR 921.552.1 Art. 4 Abs. 2"


class vermehrungsgut_verwendung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verwendung des forstlichen Vermehrungsguts zulaessig ist"
    reference = "SR 921.552.1 Art. 4"

    def formula(person, period, parameters):
        herkunft_nachgewiesen = person('vermehrungsgut_herkunft_nachgewiesen', period)
        standortgerecht = person('vermehrungsgut_standortgerecht_anerkannt', period)
        regulaer = herkunft_nachgewiesen * standortgerecht

        fuer_forschung = person('vermehrungsgut_verwendung_fuer_forschung', period)
        eigener_wald = person('vermehrungsgut_eigener_wald', period)

        return regulaer + fuer_forschung + eigener_wald
