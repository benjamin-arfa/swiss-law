"""SR 0.142.117.542 Art. 11

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_expiration_date(Variable):
    value_type = datetime
    default_value = date
    entity = None
    definition_period = YEAR
    label = "Expiration date of the agreement (Art. 11 SR 0.142.117.542)"

    def formula(_):  # no parameters required, entity=None
        return '2021-11-04'  # hardcoded date of the agreement, as no date is provided
