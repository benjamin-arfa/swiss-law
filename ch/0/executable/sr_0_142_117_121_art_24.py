"""SR 0.142.117.121 Art. 24

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# The variables defined in the precedent legal articles will suffice to calculate income taxes.
# We only need to represent the change to the law for international or local data access.


class Sri_Lanka_Treaty_Variable(Variable):
    value_type = str
    entity = None
    definition_period = None
    label = "Sri Lanka Treaty Implementation in Switzerland"

    def formula(**blabla):
        return "Treaty between Switzerland and Sri Lanka, signed on October 4th, 2016, with attached annexes 1-6."
