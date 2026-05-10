"""SR 195.1 Art. 43

Generated from: ch/195/de/195.1.md

Beschraenkung des konsularischen Schutzes: Kein Rechtsanspruch,
Verweigerungsgruende.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gefahr_fuer_aussenpolitische_interessen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Hilfeleistung aussenpolitischen Interessen nachteilig sein koennte"
    reference = "SR 195.1 Art. 43 Abs. 2 lit. a"


class andere_personen_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob andere Personen durch die Hilfeleistung gefaehrdet werden"
    reference = "SR 195.1 Art. 43 Abs. 2 lit. b"


class hat_empfehlungen_missachtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Empfehlungen des Bundes missachtet oder sich fahrlaessig verhalten hat"
    reference = "SR 195.1 Art. 43 Abs. 2 lit. c"


class hat_fruehere_hilfeleistungen_missbraucht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fruehere Hilfeleistungen missbraucht hat"
    reference = "SR 195.1 Art. 43 Abs. 2 lit. d"


class leib_und_leben_in_gefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Leib und Leben der betroffenen Person in Gefahr sind"
    reference = "SR 195.1 Art. 43 Abs. 3"


class konsularischer_schutz_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der konsularische Schutz verweigert oder begrenzt werden kann"
    reference = "SR 195.1 Art. 43 Abs. 2-3"

    def formula(person, period, parameters):
        a = person('gefahr_fuer_aussenpolitische_interessen', period)
        b = person('andere_personen_gefaehrdet', period)
        c = person('hat_empfehlungen_missachtet', period)
        d = person('hat_fruehere_hilfeleistungen_missbraucht', period)
        leib_leben = person('leib_und_leben_in_gefahr', period)
        # Verweigerung moeglich wenn ein Grund vorliegt, ABER nicht wenn Leib und Leben in Gefahr
        verweigerungsgrund = a + b + c + d > 0
        return verweigerungsgrund * (1 - leib_leben)
