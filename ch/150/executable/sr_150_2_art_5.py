"""SR 150.2 Art. 5

Generated from: ch/150/de/150.2.md

Informationsgesuch: Personen, die eine nahestehende Person vermissen und
befuerchten, dass diese verschwunden ist, koennen ein schriftliches
Informationsgesuch bei der Koordinationsstelle des Bundes einreichen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermisst_nahestehende_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine nahestehende Person vermisst"
    reference = "SR 150.2 Art. 5 Abs. 1"


class befuerchtet_verschwindenlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person befuerchtet, dass die vermisste Person verschwunden ist"
    reference = "SR 150.2 Art. 5 Abs. 1"


class kann_informationsgesuch_einreichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein Informationsgesuch einreichen kann"
    reference = "SR 150.2 Art. 5"

    def formula(person, period, parameters):
        return (
            person('vermisst_nahestehende_person', period)
            * person('befuerchtet_verschwindenlassen', period)
        )
