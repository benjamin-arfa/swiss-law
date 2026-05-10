"""SR 836.24 Art. 1

Generated from: ch/836/de/836.24.md

Art. 1: Mindestansätze für Familienzulagen - Price adjustment ordinance.
Sets the current minimum amounts for family allowances as of 2025:
- Kinderzulage: 215 CHF/month
- Ausbildungszulage: 268 CHF/month
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindestansatz_kinderzulage_2025(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Mindestansatz Kinderzulage ab 1. Jan. 2025: 215 CHF/Monat "
        "(Art. 1 Abs. 1 V Anpassung Familienzulagen)"
    )
    reference = "SR 836.24 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return 215.0


class mindestansatz_ausbildungszulage_2025(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Mindestansatz Ausbildungszulage ab 1. Jan. 2025: 268 CHF/Monat "
        "(Art. 1 Abs. 2 V Anpassung Familienzulagen)"
    )
    reference = "SR 836.24 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return 268.0
