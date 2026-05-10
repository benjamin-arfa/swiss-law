"""SR 0.641.751.411 Art. 1 - Applicable law for environmental taxes

CH-Liechtenstein agreement on environmental taxes.
Art. 1: Liechtenstein adopts Swiss federal environmental tax legislation.
- Par. 5: Liechtenstein must enact penalties at least equivalent to Swiss law.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entreprise_soumise_taxes_environnementales_li(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Enterprise subject to environmental taxes in Liechtenstein (Art. 1)"
    default_value = False


class legislation_ch_applicable_li(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Swiss federal environmental tax legislation applies to Liechtenstein (Art. 1 par. 1)"

    def formula(person, period, parameters):
        return person("entreprise_soumise_taxes_environnementales_li", period)


class peines_li_equivalentes_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Liechtenstein penalties are at least equivalent to Swiss law (Art. 1 par. 5)"
    default_value = True
