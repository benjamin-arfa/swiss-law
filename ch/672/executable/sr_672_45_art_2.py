"""SR 672.45 Art. 2

Generated from: ch/672/de/672.45.md

Verordnung des EFD über die Verzinsung ausstehender Quellensteuerbeträge
Art. 2 - Inkrafttreten
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_verzinsungsverordnung_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verordnung über die Verzinsung ausstehender Quellensteuerbeträge ist in Kraft (seit 20. Dezember 2012, zusammen mit dem IQG)"
    reference = "SR 672.45 Art. 2"

    def formula_2012_12(person, period, parameters):
        return True
