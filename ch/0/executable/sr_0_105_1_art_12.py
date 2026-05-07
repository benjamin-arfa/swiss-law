"""SR 0.105.1 Art. 12

Generated from: ch/0/de/0.105.1.md
"""

Note: Entity and variable names are conceptual and not necessarily corresponding to the exact terminology used in the article.

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class article_12_duty_a(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Duty a) allowing the SCP into the country"

    def formula(countries, period, parameters):
        return countries("scp_access", period)

class article_12_duty_b(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Duty b) providing information to SCP"

    def formula(countries, period, parameters):
        return countries("information_provided_scp", period)

class article_12_duty_c(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Duty c) promoting and facilitating contacts between SCP and national prevention mechanisms"

    def formula(countries, period, parameters):
        return countries("contacts_promoted_scp", period)

class article_12_duty_d(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Duty d) reviewing SCP's recommendations and engaging in a dialogue"

    def formula(countries, period, parameters):
        return countries("recommendations_reviewed_scp", period)
