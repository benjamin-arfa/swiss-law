"""SR 0.142.116.637 Art. 5

Generated from: ch/0/de/0.142.116.637.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_stagiaire(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Stagiaire status (Art. 5 SR)"

    def formula(person, period, parameters):
        stagiaire_id = person("stagiaire_approval_id", period)
        return stagiaire_id is not None
