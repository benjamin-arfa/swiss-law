"""SR 744.211 Art. 27

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_211_art_27_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.211 Art. 27 – Verordnung in Kraft (ab 20. Juli 1951)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1951/752_776_732/de#art_27"

    def formula(person, period, parameters):
        return period.start.date >= periods.period("1951-07-20").start.date
