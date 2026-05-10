"""SR 0.103.3 Art. 22

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ecsr_reporting_obligation(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD
    label = "Obligation to report about Freedom deprivation according ECSR Art. 22"

    def formula(person, period, parameters):
        reporting_issue_issue_a = person("ecsr_article_22_reporting_issue_a", period)
        reporting_issue_issue_b = person("ecsr_article_22_reporting_issue_b", period)
        reporting_issue_issue_c = person("ecsr_article_22_reporting_issue_c", period)

        return (reporting_issue_issue_a | reporting_issue_issue_b | reporting_issue_issue_c)
