"""SR 0.103.2 Art. 39

Generated from: ch/0/de/0.103.2.md
"""

The variable below represents the entity which the commission represents. Thus it is not directly implementable with the current information but is mentioned here to fulfill the task description.

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Institution


class commission_operational(Variable):
    value_type = bool
    entity = Institution
    definition_period = YEAR
    label = "Is the commission operational (SR 0.103.2 Art. 39)?"
