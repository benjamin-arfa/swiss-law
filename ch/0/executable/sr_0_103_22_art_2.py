"""SR 0.103.22 Art. 2

Generated from: ch/0/de/0.103.22.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries import countries


class international_reservation(Notification):
    entity = countries.all
    definition_period = YEAR
    label = "International reservation notification (SR 0.103.22 Art. 2)"

    def formula(notified_country, period, parameters):
        # Logic for communication is external, OpenFisca focuses on entities and evaluations
        return notified_country("international_reservation", period)
