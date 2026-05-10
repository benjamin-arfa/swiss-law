"""SR 0.142.113.672 Art. 27

Generated from: ch/0/de/0.142.113.672.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class article_27_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "ART. 27 eligibility (SR 0.142.1.136.2 Art. 27)"

    def formula(person, period, parameters):
        european_regulations = (parameters(period).social_security.european_regulations.legacy_regulations
            .apply_to(person, period).combine_first(parameters(period).social_security
                .european_regulations.current_regulations.apply_to(person, period)))
        cutoff_date = period.last_month.date().replace(day=31)
        eligible = (cutoff_date < person("birth_date")) | (
            (cutoff_date <= period.date.date()) &
            ((european_regulations.prev) | (person("ahv_eligibility_date", period)) >= cutoff_date))
        return eligible
