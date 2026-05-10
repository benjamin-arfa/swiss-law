"""SR 0.103.3 Art. 13

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class can_grant_extradition_request(Boolean):
    label = "Can grant extradition request for enforced disappearance (Art. 13)"

    def formula(extradition_request, period, parameters):
        request_reason = extradition_request("request_reason", period)
        is_enforced_disappearance = extradition_request("is_enforced_disappearance", period)

        # Condition 1: Request reason is not for pursuing or punishing a person for their gender, race, religion, nationality, ethnicity, political beliefs or social group membership.
        # This condition is parameterized, as the list of protected characteristics may not be exhaustive.
        protected_characteristics = parameters(period).extradition.request_reason_exemptions

        exempt_reasons = extradite_reasons.filter(lambda reason: reason not in protected_characteristics)

        # Condition 2: Ersuchender Staat hat stichhaltige Gründe für die Annahme, dass das Ersuchen gestellt worden ist:
        # - zur Verfolgung oder Bestrafung einer Person wegen ihres Geschlechts, ihrer Rasse, ihrer Religion, ihrer Staatsangehörigkeit
        # - ihrer ethnischen Herkunft, ihrer politischen Anschauungen oder ihrer Zugehörigkeit zu einer bestimmten sozialen Gruppe
        # oder
        # - um dieser Person aus einem dieser Gründe Schaden zugefügt werden zu können

        # This condition is not parameterizable, as it is a strict limitation.

        return request_reason not in exempt_reasons
