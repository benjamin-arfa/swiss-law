"""SR 832.208 Art. 2

Generated from: ch/832/de/832.208.md

Prämienzuschlag für Verhütung von Nichtberufsunfällen.
Rate: 0.75% (3/4%) of net premiums for non-occupational accident insurance.
In force since 1 January 1994.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR


class uv_praemienzuschlag_nichtberufsunfall(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prämienzuschlag für Verhütung von Nichtberufsunfällen (Anteil)"
    reference = "SR 832.208 Art. 2"

    def formula_1994(person, period, parameters):
        return parameters(period).sr832_208.praemienzuschlag_nichtberufsunfall
