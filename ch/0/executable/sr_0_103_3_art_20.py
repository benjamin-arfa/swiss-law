"""SR 0.103.3 Art. 20

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class restricted_info_rights(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Rights to information are restricted (Art. 20 SR 0.103.3)"

    def formula(person, period, parameters):
        restrictions_apply = (  # check all conditions for restrictions
            (not person("is_under_lawful_protection", period)) |  # if protection not applied
            (not person("liberty_under_judicial_control", period))  # if liberty not under judicial control, or other condition applies
        )

        returns_to_liberty_right = (  # if person returns after liberty deprivation
            person("liberty_return_date", period) < period.last_day
        )

        has_judicial_recourse = person("has_judicial_recourse", period)

        has_privacy_threat = person("has_privacy_threat", period)  # privacy at risk
        has_security_threat = person("has_security_threat", period)  # security at risk
        has_evidence_delay = person("has_evidence_delay", period)  # holds up investigation

        return (restrictions_apply) & (has_judicial_recourse & returns_to_liberty_right & has_privacy_threat & has_security_threat & has_evidence_delay)
        return (~returns_to_liberty_right & (has_privacy_threat | has_evidence_delay | other_equivalent_grounds))
