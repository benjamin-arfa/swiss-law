"""SR 0.142.117.149 Art. 6

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transfer_request_obligation_deadline_met(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Deadline met for transfer request due to detected unauthorized entry or residence (Art. 6 SR 0.142.117.149)"

    def formula(person, period, parameters):
        unauthorized_entry_detection_date = person("unauthorized_entry_detection_date", period)
        unauthorized_residence_detection_date = person("unauthorized_residence_detection_date", period)

        one_year_duration = 365  # in days approximated as an exact value

        if unauthorized_entry_detection_date is None and unauthorized_residence_detection_date is None:
            return True  # Deadlines should be set when a detection occurs
        elif unauthorized_entry_detection_date is not None and unauthorized_residence_detection_date is not None:
            min_detection_date = min(unauthorized_entry_detection_date, unauthorized_residence_detection_date)

            from_date = min_detection_date
            to_date = min_detection_date + one_year_duration
            today = period.last_date('overall')

            within_deadline = (
                (from_date <= today) &
                (today <= to_date)
            )
            return not within_deadline
        else:
          # When there is only one type of detection date available, there is no deadline for submission
            return True
