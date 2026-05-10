"""SR 0.142.115.722 Art. 3

Generated from: ch/0/de/0.142.115.722.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bilateral_va_validity(Variable):
    value_type = int
    label = "Validity of bilateral VA in years (Art. 3 SR 0.142.115.722)"

    def formula(_period):
        return 3
