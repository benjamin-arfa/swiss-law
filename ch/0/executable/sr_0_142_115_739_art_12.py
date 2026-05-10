"""SR 0.142.115.739 Art. 12

Generated from: ch/0/de/0.142.115.739.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mistakenly_taken_back(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD('entry_date', 'entry_date')
    label = "Person mistakenly taken back in deportation (Art. 12 SR 0.142.115.739)"

    def formula(person, period, parameters):
        entry_date = person("entry_date", period)
        deportation_status = person("deportation_status", period)
        conditions_met = person("conditions_met_articles_2_to_5", period)
        time_frame = (entry_date + period.duration).shift(months=6)

        return deportation_status & ~conditions_met & (entry_date <= time_frame)
