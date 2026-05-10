"""SR 0.192.110.978.41 Art. 5

Generated from: ch/0/de/0.192.110.978.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class allow_currency_assets(Variable):
    value_type = bool
    entity = EutelsatOrganization
    label = "EUTELSAT allowed to receive, possess, and manage various financial instruments"

    def formula(eutelsat, period, parameters):
        # This variable seems not to be dependent on the period
        allowed_status = parameters(period).eutelsat.allowed_status
        return allowed_status
