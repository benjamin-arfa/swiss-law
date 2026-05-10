"""SR 0.103.2 Art. 40

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class country_reporting_obligation(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Obligation for countries to submit periodic reports on Covenant implementation"

    def formula(country, period, parameters):
        treaty_entry_year = parameters(period).international_treaties.covenant_entry_year
        initial_reporting_due_date = month(treaty_entry_year + 1)

        is_previous_year = (month(period.start.date) == initial_reporting_due_date)

        subsequent_reporting_due = period.index_in_period > 0

        return (is_previous_year | subsequent_reporting_due)

class country_report_transmitted_report(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Country has transmitted its periodic report for the Covenant"

    def formula(country, period, parameters):
        treaty_entry_year = parameters(period).international_treaties.covenant_entry_year
        initial_reporting_due_date = month(treaty_entry_year + 1)

        is_previous_year = (month(period.start.date) == initial_reporting_due_date)

        has_submitted_request_to_committee = country("has_submitted_request_to_committee", period)

        return has_submitted_request_to_committee

class country_committee_reporting(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "The Committee has published a report for the country on Covenant implementation"

    def formula(country, period, parameters):
        treaty_entry_year = parameters(period).international_treaties.covenant_entry_year
        initial_reporting_due_date = month(treaty_entry_year + 1)

        has_submitted_report = country("has_submitted_country_report", period)
        general_comments_received = country("general_comments_received", period)

        return has_submitted_report & general_comments_received

class has_submitted_request_to_committee(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "The country has submitted a request to the Committee for a report on Covenant implementation"

    def formula(country, period, parameters):
        treaty_entry_year = parameters(period).international_treaties.covenant_entry_year
        initial_reporting_due_date = month(treaty_entry_year + 1)

        is_previous_year = (month(period.start.date) == initial_reporting_due_date)

        return is_previous_year

class has_submitted_country_report(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "The country has submitted its periodic report on Covenant implementation"

    def formula(country, period, parameters):
        has_submitted_request_to_committee_value = country("has_submitted_request_to_committee", period)
        country_obligation_variable = country("country_reporting_obligation", period)

        return has_submitted_request_to_committee_value & country_obligation_variable

class general_comments_received(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "The Committee has received its comments on the country report"

    def formula(country, period, parameters):
        has_submitted_report_value = country("has_submitted_country_report", period)
        country_obligation_variable = country("country_reporting_obligation", period)

        return has_submitted_report_value & country_obligation_variable
