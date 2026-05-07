"""SR 653.1 Art. 1

Generated from: ch/653/de/653.1.md
Subject: The AIAG regulates automatic exchange of information in tax matters
between Switzerland and partner states, covering financial accounts (CRS/GMS)
and crypto assets (MRK).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class is_subject_to_aeoi(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the entity is subject to automatic exchange of information (AEOI/AIA)"
    reference = "SR 653.1 Art. 1"

    def formula(person, period, parameters):
        financial_accounts = person("holds_reportable_financial_accounts", period)
        crypto_assets = person("holds_reportable_crypto_assets", period)
        partner_state = person("has_partner_state_connection", period)
        return (financial_accounts + crypto_assets) * partner_state
