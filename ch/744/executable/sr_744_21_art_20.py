"""SR 744.21 Art. 20

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_21_art_20_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.21 Art. 20 – Gesetz ist in Kraft getreten (ab 20. Juli 1951)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1951/752_755_744/de#art_20"

    def formula(person, period, parameters):
        # Law entered into force on 20 July 1951 per Federal Council decree of 6 July 1951
        return period.start.year > 1951 or (period.start.year == 1951 and period.start.month >= 7)
