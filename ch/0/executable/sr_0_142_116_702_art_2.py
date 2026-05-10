"""SR 0.142.116.702 Art. 2

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schengen_visafree_residency(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for visa-free residency in Switzerland (Article 2)"

    def formula(person, period, parameters):
        return person("has_diplomatic_or_official_passport", period) | \
               person.schengen_visited_last_180_days == False


class schengen_visited_last_180_days(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has visited Schengen zone in the last 180 days"

    def formula(person, period, parameters):
        foreign_nations = parameters(period).foreign_nations
        dates = [parameters(period).foreign_nation_visits[n] for n in foreign_nations]
        visits_last_180days = sum(1 for date in dates if date.in_period(period))
        return visits_last_180days > 1
