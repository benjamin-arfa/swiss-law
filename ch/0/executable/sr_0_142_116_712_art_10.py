"""SR 0.142.116.712 Art. 10

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

import datetime


class suspension_grounds(Variable):
    value_type = str
    definition_period = YEAR
    label = "Suspension grounds for international treaty (Article 10 SR 0.142.116.712)"

    def formula(suspended_party, period, parameters):
        grounds_occurrence = parameters(period).international_treaty_art_10.suspension_grounds
        return grounds_occurrence
