"""SR 138.1 Art. 6

Generated from: ch/138/de/138.1.md

Vertraulichkeit der Informationen: Confidential treatment of information
must be guaranteed.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class vertrauliche_behandlung_gewaehrleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die vertrauliche Behandlung der Informationen ist gewaehrleistet"
    reference = "SR 138.1 Art. 6"
