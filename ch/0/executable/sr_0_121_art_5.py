"""SR 0.121 Art. V

Generated from: ch/0/de/0.121.md

Nuclear explosions and radioactive waste disposal are prohibited
in Antarctica.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_kernexplosionen_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kernexplosionen in der Antarktis verboten sind"
    reference = "SR 0.121 Art. V Abs. 1"

    def formula(person, period, parameters):
        return 1


class antarktis_radioaktiver_abfall_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beseitigung radioaktiven Abfalls in der Antarktis verboten ist"
    reference = "SR 0.121 Art. V Abs. 1"

    def formula(person, period, parameters):
        return 1
