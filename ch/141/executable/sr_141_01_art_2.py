"""SR 141.01 Art. 2

Generated from: ch/141/de/141.01.md

Vertrautsein mit den schweizerischen Lebensverhältnissen bei einer
ordentlichen Einbuergerung: Grundkenntnisse Geografie/Geschichte/Politik,
Teilnahme am sozialen/kulturellen Leben, Kontakte zu Schweizern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class grundkenntnisse_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Grundkenntnisse der geografischen, historischen, politischen und gesellschaftlichen Verhaeltnisse der Schweiz vorliegen"
    reference = "SR 141.01 Art. 2 Abs. 1 Bst. a"


class teilnahme_soziales_kulturelles_leben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob am sozialen und kulturellen Leben der Gesellschaft in der Schweiz teilgenommen wird"
    reference = "SR 141.01 Art. 2 Abs. 1 Bst. b"


class kontakte_zu_schweizern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kontakte zu Schweizerinnen und Schweizern gepflegt werden"
    reference = "SR 141.01 Art. 2 Abs. 1 Bst. c"


class vertraut_mit_lebensverhaeltnissen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bewerberin oder der Bewerber mit den schweizerischen Lebensverhaeltnissen vertraut ist"
    reference = "SR 141.01 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        grundkenntnisse = person('grundkenntnisse_schweiz', period)
        sozial_kulturell = person('teilnahme_soziales_kulturelles_leben', period)
        kontakte = person('kontakte_zu_schweizern', period)
        return grundkenntnisse * sozial_kulturell * kontakte
