"""SR 0.142.117.587 Art. 4

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class work_permit_application_status(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Status of work permit application for young professionals (Art. 4, SR 0.142.117.587)"

    def formula(person, period, parameters):
        # Assume initial status as unprocessed
        return 1 - person("work_permit_application_processing_status", period)


class work_permit_application_processing_status(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Processing status of work permit application for young professionals (Art. 4, SR 0.142.117.587)"

    def formula(person, period, parameters):
        # Awaiting application submission (default)
        waiting_for_submission = person("documents_sent_to_authority", period)
        waiting_for_submission *= waiting_for_submission == 0

        # Application submitted
        submission_sent = person("documents_sent_to_authority", period)
        submitted = submission_sent > 0

        # Processing by home country authority (Article 9)
        processing_by_home_country = person("application_forwarded_to_host_country", period)
        processing_by_home_country *= processing_by_home_country == 0

        # Waiting for approval by host country authority (Art. 4, para 3)
        awaiting_approval = person("application_forwarded_to_host_country", period)
        awaiting_approval *= awaiting_approval > 0

        # Approved and work permit issued (Art. 4, paras 4-5)
        approved = person("work_permit_issued", period)
        approved *= approved == 1

        status = (submitted | processing_by_home_country | awaiting_approval | approved)
        return status


class work_permit_issued(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Work permit issued for young professional (Art. 4, SR 0.142.117.587, para. 4-5)"

    def formula(person, period, parameters):
        issued = (person("valid_work_permit", period) == 1)
        return issued


class documents_sent_to_authority(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Documents sent to home country authority for work permit application (Art. 4, SR 0.142.117.587)"

    def formula(person, period, parameters):
        # A function to initialize the variable (set value to 0)
        return 0


class application_forwarded_to_host_country(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Application forwarded to host country authority for work permit (Art. 4, SR 0.142.117.587, para. 3)"

    def formula(person, period, parameters):
        forwarded = (person("application_forwarded", period) == 1)
        return forwarded
