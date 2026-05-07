"""SR 0.142.116.909 Art. 19

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person
from openfisca_core.periods import DAY

class submission_method(event.Event):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Submission of employment related documents via secure means (Art. 19 SR 0.142.116.909)"

    def method(person, period, parameters):
        return True
