"""SR 744.21 Art. 19a

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pending_application_subject_to_new_procedure(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pending application at entry into force is subject to new procedural law (SR 744.21 Art. 19a para. 1)"
    reference = "SR 744.21 Art. 19a Abs. 1"

    def formula(person, period, parameters):
        application_pending_at_entry_into_force = person('application_pending_at_entry_into_force', period)
        is_application = person('is_application_not_appeal', period)
        return application_pending_at_entry_into_force * is_application


class pending_appeal_subject_to_old_procedure(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pending appeal at entry into force is subject to old procedural law (SR 744.21 Art. 19a para. 2)"
    reference = "SR 744.21 Art. 19a Abs. 2"

    def formula(person, period, parameters):
        application_pending_at_entry_into_force = person('application_pending_at_entry_into_force', period)
        is_appeal = person('is_appeal', period)
        return application_pending_at_entry_into_force * is_appeal


class application_pending_at_entry_into_force(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Application or appeal was pending at the time of entry into force of the amendment"
    reference = "SR 744.21 Art. 19a"


class is_application_not_appeal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "The pending proceeding is an application (Gesuch), not an appeal (Beschwerde)"
    reference = "SR 744.21 Art. 19a Abs. 1"


class is_appeal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "The pending proceeding is an appeal (Beschwerde)"
    reference = "SR 744.21 Art. 19a Abs. 2"
