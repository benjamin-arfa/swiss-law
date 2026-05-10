"""SR 935.61 Art. 17

Generated from: ch/935/de/935.61.md

Art. 17: Disziplinarmassnahmen
1. Bei Verletzung dieses Gesetzes kann die Aufsichtsbehörde anordnen:
   a. Verwarnung
   b. Verweis
   c. Busse bis zu 20'000 Franken
   d. Befristetes Berufsausübungsverbot für längstens zwei Jahre
   e. Dauerndes Berufsausübungsverbot
2. Busse kann zusätzlich zu Berufsausübungsverbot angeordnet werden
3. Vorsorgliches Berufsausübungsverbot möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class DisziplinarmassnahmeEnum(Enum):
    keine = "Keine Massnahme"
    verwarnung = "Verwarnung"
    verweis = "Verweis"
    busse = "Busse"
    befristetes_verbot = "Befristetes Berufsausübungsverbot"
    dauerndes_verbot = "Dauerndes Berufsausübungsverbot"


class anwalt_disziplinarmassnahme(Variable):
    value_type = bool
    possible_values = DisziplinarmassnahmeEnum
    default_value = DisziplinarmassnahmeEnum.keine
    entity_key = 'person'
    definition_period = YEAR
    label = "Verhängte Disziplinarmassnahme nach Art. 17 BGFA"
    reference = "SR 935.61 Art. 17 Abs. 1"


class anwalt_busse_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der Busse in CHF (maximal 20'000)"
    reference = "SR 935.61 Art. 17 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        busse_roh = person('anwalt_busse_betrag_roh', period)
        max_busse = parameters(period).sr_935_61.max_busse_chf
        return np.minimum(busse_roh, max_busse)


class anwalt_busse_betrag_roh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beantragte/festgesetzte Busse vor Plafonnierung"
    reference = "SR 935.61 Art. 17 Abs. 1 Bst. c"


class anwalt_berufsverbot_dauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer des befristeten Berufsausübungsverbots in Monaten (max. 24)"
    reference = "SR 935.61 Art. 17 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        dauer_roh = person('anwalt_berufsverbot_dauer_monate_roh', period)
        max_monate = parameters(period).sr_935_61.max_berufsverbot_monate
        return np.minimum(dauer_roh, max_monate)


class anwalt_berufsverbot_dauer_monate_roh(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Beantragte Dauer des Berufsausübungsverbots in Monaten vor Plafonnierung"
    reference = "SR 935.61 Art. 17 Abs. 1 Bst. d"


class anwalt_vorsorgliches_verbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vorsorgliches Berufsausübungsverbot angeordnet"
    reference = "SR 935.61 Art. 17 Abs. 3"
