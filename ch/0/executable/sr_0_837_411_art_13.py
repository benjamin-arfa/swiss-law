"""SR 0.837.411 Art. 13 - Form of payment

Art. 13:
- Par. 1: Indemnities must be paid in cash; supplementary in-kind benefits
  to facilitate re-employment are allowed.
- Par. 2: Allowances may be provided in kind.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class indemnite_payee_especes(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Indemnity is paid in cash (mandatory per Art. 13 par. 1)"

    def formula(person, period, parameters):
        # Art. 13 par. 1: Indemnities MUST be paid in cash
        return person("systeme_indemnite_chomage", period)


class allocation_en_nature_autorisee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Allowance may be provided in kind (Art. 13 par. 2)"

    def formula(person, period, parameters):
        return person("systeme_allocation_chomage", period)
