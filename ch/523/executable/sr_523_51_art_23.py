"""SR 523.51 Art. 23

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beschwerde_frist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Beschwerdefrist in Tagen gegen die Bewertung eines Moduls"
    reference = "SR 523.51 Art. 23 Abs. 2"

    def formula(person, period, parameters):
        # 30 days from notification
        return person.filled_array(30)
