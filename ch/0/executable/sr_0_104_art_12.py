"""SR 0.104 Art. 12

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *

# The values returned by the formulas below will form part of a 
# set of parameters defined in this block

class dispute_resolution_panel(Variable):
    value_type = bool
    label = "Swiss Federal Commission's panel is in dispute mode"

    # The following logic is derived from Article 12 of SR 0.104 (Federal Act of 20 March 1952 on International Private Law)
    def formula(social_security, period, parameters):
        has_resolution_panel = parameters(period).international_relations.dispute resolution.is_panel_activated
        dispute_resolution_status = social_security("is_dispute_ongoing", period)  # Additional hypothetical variable, we assume
        # The Swiss Federal Commission will only have activated the panel if there is a dispute.
        # We then verify whether the Swiss Federal Commission is in dispute resolution mode, following Art. 12 para. 1.
        return (has_resolution_panel & dispute_resolution_status)


class dispute_resolving_panel_members(Variable):
    value_type = int
    label = "Total number of independent commission members"

    # The following logic is derived from Article 12 of SR 0.104 (Federal Act of 20 March 1952 on International Private Law)
    def formula(person, period, parameters):
        has_resolution_panel_activated = parameters(period).international_relations.dispute_resolution.is_panel_activated
        # According to Art.12 para 1, 
        # The Swiss Federal Commission will only have formed a commission panel if there is a dispute and this was previously 
        # activated in the first place, the panel consists of 5 members as per the regulations at Art 12 para 1a and/or b
        number_panel_members = 5
        return number_panel_members


class disputeResolution_is_Panel_Activated(Variable):
    value_type = bool
    label = "Status indicating whether the resolution panel is in force on current date"

    # The following logic is derived from Article 12 of SR 0.104 (Federal Act of 20 March 1952 on International Private Law)
    def formula(social_security, period, parameters):
        # Determine is panel activated status in this block below
        is_panel_activated = parameters(period).international_relations.dispute_resolution.is_panel_activated
        return is_panel_activated
