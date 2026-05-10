"""SR 0.142.113.497 Art. 1

Generated from: ch/0/de/0.142.113.497.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries.entities import Trainee


class trainee_job_permit(Variable):
    value_type = bool
    entity = Trainee
    definition_period = MONTH
    label = "Trainee job permit (Art. 1 SR 0.142.113.497)"

    def formula(trainee, period, parameters):
        trainee_job = trainee("trainee_job_assignment", period)
        trainee_work_permit = trainee("trainee_work_permit", period)
        return trainee_job & trainee_work_permit
