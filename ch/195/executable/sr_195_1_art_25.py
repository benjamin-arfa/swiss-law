"""SR 195.1 Art. 25

Generated from: ch/195/de/195.1.md

Mehrfache Staatsangehoerigkeit: In der Regel keine Sozialhilfe wenn die
auslaendische Staatsangehoerigkeit vorherrscht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_mehrfache_staatsangehoerigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person mehrere Staatsangehoerigkeiten besitzt"
    reference = "SR 195.1 Art. 25"


class auslaendische_staatsangehoerigkeit_herrscht_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die auslaendische Staatsangehoerigkeit vorherrscht"
    reference = "SR 195.1 Art. 25"


class sozialhilfe_ausgeschlossen_mehrfach_staatsangehoerigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sozialhilfe wegen vorherrschender auslaendischer Staatsangehoerigkeit in der Regel ausgeschlossen ist"
    reference = "SR 195.1 Art. 25"

    def formula(person, period, parameters):
        mehrfach = person('hat_mehrfache_staatsangehoerigkeit', period)
        vorherrschend = person('auslaendische_staatsangehoerigkeit_herrscht_vor', period)
        return mehrfach * vorherrschend
