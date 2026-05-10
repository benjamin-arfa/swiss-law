"""SR 282.11 Art. 44 - Beschwerde gegen Beiratschaftsverfuegungen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beschwerdefrist_gegen_beiratschaft_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Beschwerde gegen Verfuegungen der Beiratschaft in Tagen"
    reference = "SR 282.11 Art. 44"

    def formula(self, period, parameters):
        return 10
