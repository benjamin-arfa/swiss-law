"""SR 523.51 Art. 1

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 1: This ordinance regulates the training of teaching staff for
# leadership bodies and civil protection.


class ist_lehrpersonal_fuehrungsorgane(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Lehrpersonal fuer die Fuehrungsorgane"
    reference = "SR 523.51 Art. 1"


class ist_lehrpersonal_zivilschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Lehrpersonal fuer den Zivilschutz"
    reference = "SR 523.51 Art. 1"
