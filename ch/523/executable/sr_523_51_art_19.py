"""SR 523.51 Art. 19

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ausbildungsangebot_frist_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Ausbildungsangebot wurde spaetestens in der Kalenderwoche 32 zugestellt"
    reference = "SR 523.51 Art. 19"
