"""SR 653.1 Art. 2

Generated from: ch/653/de/653.1.md
Definitions: Key terms including existing/new accounts, low/high value accounts,
Swiss financial institutions, crypto service providers, and tax identification numbers.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class is_high_value_account(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether account is a high-value existing account (> USD 1M)"
    reference = "SR 653.1 Art. 2 Abs. 1 lit. l"

    def formula(person, period, parameters):
        is_existing = person("is_existing_financial_account", period)
        is_natural = person("is_natural_person_account", period)
        balance = person("account_balance_usd", period)
        return is_existing * is_natural * (balance > 1000000)


class is_low_value_account(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether account is a low-value existing account (<= USD 1M)"
    reference = "SR 653.1 Art. 2 Abs. 1 lit. k"

    def formula(person, period, parameters):
        is_existing = person("is_existing_financial_account", period)
        is_natural = person("is_natural_person_account", period)
        balance = person("account_balance_usd", period)
        return is_existing * is_natural * (balance <= 1000000)


class is_swiss_financial_institution(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether entity qualifies as a Swiss financial institution under AIAG"
    reference = "SR 653.1 Art. 2 Abs. 1 lit. d"

    def formula(person, period, parameters):
        resident_fi = person("is_resident_financial_institution", period)
        is_branch_abroad = person("is_foreign_branch_of_swiss_fi", period)
        is_swiss_branch = person("is_swiss_branch_of_foreign_fi", period)
        # Swiss FI = resident FI (excl. foreign branches) OR Swiss branches of foreign FIs
        return (resident_fi * not_(is_branch_abroad)) + is_swiss_branch
