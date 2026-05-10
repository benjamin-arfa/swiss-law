"""SR 210 Art. 31

Generated from: ch/de/210.md

Anfang der Persoenlichkeit: Die Persoenlichkeit beginnt mit dem Leben nach
der vollendeten Geburt und endet mit dem Tode. Vor der Geburt ist das Kind
unter dem Vorbehalt rechtsfaehig, dass es lebendig geboren wird.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_lebend_geboren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person lebendig geboren wurde"
    reference = "SR 210 Art. 31 Abs. 1"
    default_value = True


class ist_persoenlichkeit_begonnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Persoenlichkeit begonnen hat (Leben nach vollendeter Geburt)"
    reference = "SR 210 Art. 31"

    def formula(person, period, parameters):
        ist_geboren = person('ist_lebend_geboren', period)
        ist_verstorben = person('ist_verstorben', period)
        # Persoenlichkeit beginnt mit Geburt, endet mit Tod
        return ist_geboren * not_(ist_verstorben)


class ist_verstorben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person verstorben ist"
    reference = "SR 210 Art. 31 Abs. 1"
