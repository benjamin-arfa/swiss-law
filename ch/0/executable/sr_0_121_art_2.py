"""SR 0.121 Art. II

Generated from: ch/0/de/0.121.md

Freedom of scientific investigation in Antarctica and cooperation toward
that end shall continue, subject to the provisions of this Treaty.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_freiheit_wissenschaftliche_forschung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Freiheit der wissenschaftlichen Forschung in der Antarktis gilt"
    reference = "SR 0.121 Art. II"

    def formula(person, period, parameters):
        return 1
