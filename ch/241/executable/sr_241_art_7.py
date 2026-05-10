"""SR 241 Art. 7

Generated from: ch/de/241.md

Non-compliance with working conditions imposed by law or contract.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arbeitsbedingungen_nicht_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Arbeitsbedingungen nicht eingehalten werden die auch Mitbewerbern auferlegt sind"
    reference = "SR 241 Art. 7"
