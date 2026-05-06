"""SR 312.1 Art. 32

Generated from: ch/312/de/312.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class einsprache_frist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Einsprache gegen Strafbefehl (10 Tage)"
    reference = "SR 312.1 Art. 32 Abs. 5"
    default_value = 10
