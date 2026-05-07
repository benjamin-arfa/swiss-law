"""SR 0.142.116.907 Art. 3

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class stagiaires_bewilligung_awarded(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Stagiairesbewilligung has been awarded (Art. 3 SR 0.142.116.907)"

    def formula(person, period, parameters):
        return True  # the decision does not depend on any condition
