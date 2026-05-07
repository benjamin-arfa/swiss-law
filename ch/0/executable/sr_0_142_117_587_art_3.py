"""SR 0.142.117.587 Art. 3

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class swiss_young_professional_quota(Variable):
    value_type = int
    entity = Country
    definition_period = YEAR
    label = "Swiss quota for work permits for young professionals (Art. 3 SR 0.142.117.587)"


class foreign_nationals_allowed(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Switzerland: Are foreign nationals allowed under the work permit quota (Art. 3 SR 0.142.117.587)?"


class is_permit_new_extension(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is permit an extension or a new permit (Art. 3 SR 0.142.117.587)"


class permit_quota_utilization(Variable):
    value_type = float
    entity = Country
    definition_period = YEAR
    label = "Switzerland: Quota utilization rate for work permits (Art. 3 SR 0.142.117.587)"


class available_quota_units(Variable):
    value_type = int
    entity = Country
    definition_period = YEAR
    label = "Switzerland: Remaining quota units left for work permits (Art. 3 SR 0.142.117.587)"
