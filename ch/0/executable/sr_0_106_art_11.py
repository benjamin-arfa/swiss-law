"""SR 0.106 Art. 11

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class report_publication_confidential(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Require explicit consent for report publication: personal info"

    def formula(person, period, parameters):
        report_confidently = publication_confidently(person, period)
        will_publish_report = parameters(period).safeguard.committee_report_publication
        explicit_consent_required = parameters(period).safeguard.explicit_consent_required
        return report_confidently and (will_publish_report or explicit_consent_required)

class reporting_content_publication(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Public disclosure of reporting content"

    def formula(person, period, parameters):
        consent_given = person("consent_given", period)
        publication_status = parameters(period).safeguard.report_published
        return consent_given and publication_status

class visits_confidentiality(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Visit details confidentiality"

    def formula(person, period, parameters):
        visits_performed = person("visits_performed", period)
        publication_status = parameters(period).safeguard.visit_report_published
        return visits_performed and not publication_status
