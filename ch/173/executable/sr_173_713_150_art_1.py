"""SR 173.713.150 Art. 1

Generated from: ch/173/de/173.713.150.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class max_ordentliche_richter_strafkammer(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Max. Vollzeitstellen ordentliche Richter Straf-/Beschwerdekammern BStGer (Art. 1 lit. a)"
    reference = "SR 173.713.150 Art. 1"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 16

class max_nebenamtliche_richter_strafkammer(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Max. nebenamtliche Richter Straf-/Beschwerdekammern BStGer (Art. 1 lit. b)"
    reference = "SR 173.713.150 Art. 1"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 4

class max_ordentliche_richter_berufungskammer(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Max. Vollzeitstellen ordentliche Richter Berufungskammer BStGer (Art. 1 lit. c)"
    reference = "SR 173.713.150 Art. 1"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 4

class max_nebenamtliche_richter_berufungskammer(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Max. nebenamtliche Richter Berufungskammer BStGer (Art. 1 lit. d)"
    reference = "SR 173.713.150 Art. 1"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 10
