"""SR 131.216.1 Art. 1

Generated from: ch/131/de/131.216.1.md

Sovereignty: The Canton of Obwalden is a democratic free state and,
within the framework of the Federal Constitution, a sovereign canton
and federal member of the Swiss Confederation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kanton_obwalden_demokratischer_freistaat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Obwalden ein demokratischer Freistaat ist"
    reference = "SR 131.216.1 Art. 1"


class kanton_obwalden_souveraener_stand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Obwalden ein souveräner Stand der Schweizerischen Eidgenossenschaft ist"
    reference = "SR 131.216.1 Art. 1"


class kanton_obwalden_bundesglied(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Obwalden ein Bundesglied der Schweizerischen Eidgenossenschaft ist"
    reference = "SR 131.216.1 Art. 1"


class obwalden_souveraenitaet_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Souveränität des Kantons Obwalden im Rahmen der Bundesverfassung gültig ist"
    reference = "SR 131.216.1 Art. 1"

    def formula(person, period, parameters):
        return (
            person('kanton_obwalden_demokratischer_freistaat', period) *
            person('kanton_obwalden_souveraener_stand', period) *
            person('kanton_obwalden_bundesglied', period)
        )