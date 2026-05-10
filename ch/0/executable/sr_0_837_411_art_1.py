"""SR 0.837.411 Art. 1 - Unemployment benefit system types

ILO Convention No. 44 (1934) - Involuntary unemployment benefits.
Art. 1: Each ratifying member must maintain a system providing either
indemnities (contribution-based), allowances (non-contributory), or both.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class chomage_involontaire(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is involuntarily unemployed (SR 0.837.411 Art. 1)"


class systeme_indemnite_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is covered by contribution-based unemployment indemnity system (Art. 1 par. 1 let. a)"

    def formula(person, period, parameters):
        return person("chomage_involontaire", period)


class systeme_allocation_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is covered by non-contributory unemployment allowance system (Art. 1 par. 1 let. b)"

    def formula(person, period, parameters):
        return person("chomage_involontaire", period)


class assurance_chomage_obligatoire(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is covered by compulsory unemployment insurance (Art. 1 par. 2 let. a)"
    default_value = True
