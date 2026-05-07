"""SR 744.103 Art. 18

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verordnung_sr_744_103_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.103 ist in Kraft (ab 1. Januar 2016)"
    reference = "SR 744.103 Art. 18"

    def formula(person, period, parameters):
        return period.start.date >= datetime.date(2016, 1, 1)
