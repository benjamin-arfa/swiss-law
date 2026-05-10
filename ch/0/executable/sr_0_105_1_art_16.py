"""SR 0.105.1 Art. 16

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class subcommittee_report_publication(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Subcommittee report publication to Contracting State (Art. 16 SR 0.105.1)"

    def formula(countries, period, parameters):
        resides_switzerland = countries("resides_switzerland", period)
        consent_from_individual = countries("consent_from_individual", period)

        report_publishing = parameters(period).social_security.subcommittee_report_publishing
        return (resides_switzerland & report_publishing) | (consent_from_individual & report_publishing)
