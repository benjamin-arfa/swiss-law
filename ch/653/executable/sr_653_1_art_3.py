"""SR 653.1 Art. 3

Generated from: ch/653/de/653.1.md
Non-reporting financial institutions: Government entities (Confederation, cantons,
communes), international organizations, the SNB, and pension institutions
are generally non-reporting, with exceptions for commercial financial activities
and digital central bank currencies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class is_non_reporting_financial_institution(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether entity is a non-reporting financial institution under AIAG"
    reference = "SR 653.1 Art. 3"

    def formula(person, period, parameters):
        is_government = person("is_government_entity", period)
        is_intl_org = person("is_international_organization", period)
        is_central_bank = person("is_central_bank_entity", period)
        is_pension = person("is_pension_institution", period)

        # Exception: commercial financial activities make them reporting
        has_commercial_exception = person("has_commercial_financial_activities", period)
        has_cbdc_exception = person("custodies_digital_central_bank_currency", period)

        base_exempt = is_government + is_intl_org + is_central_bank + is_pension
        exception = has_commercial_exception + has_cbdc_exception

        return base_exempt * not_(exception)
