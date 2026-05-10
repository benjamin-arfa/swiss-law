"""SR 0.837.411 Art. 7 - Waiting period (delai de carence)

Art. 7: Benefit entitlement may be subject to a waiting period,
the duration and conditions of which are set by national legislation.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jours_carence_chomage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Number of waiting days before unemployment benefit starts (Art. 7)"
    default_value = 5


class delai_carence_ecoule(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Waiting period for unemployment benefit has elapsed (Art. 7)"

    def formula(person, period, parameters):
        jours_chomage = person("jours_chomage_continu", period)
        jours_carence = person("jours_carence_chomage", period)
        return jours_chomage >= jours_carence


class jours_chomage_continu(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Consecutive days of unemployment"
    default_value = 0
