"""SR 131.218 § 1

Generated from: ch/131/de/131.218.md

Democratic free state and sovereignty: The Canton of Zug is a democratic
free state. As such, insofar as cantonal sovereignty is not restricted by
the Federal Constitution, it is a sovereign federal member of the Swiss Confederation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kanton_zug_demokratischer_freistaat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Zug ein demokratischer Freistaat ist"
    reference = "SR 131.218 § 1 Abs. 1"


class kanton_zug_souveraenes_bundesglied(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Zug ein souveränes Bundesglied der Schweizerischen Eidgenossenschaft ist"
    reference = "SR 131.218 § 1 Abs. 2"


class zuger_kantonalsouveraenitaet_beschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kantonalsouveränität durch die Bundesverfassung beschränkt wird"
    reference = "SR 131.218 § 1 Abs. 2"


class zuger_souveraenitaet_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Souveränität des Kantons Zug gültig ist, soweit nicht bundesrechtlich beschränkt"
    reference = "SR 131.218 § 1"

    def formula(person, period, parameters):
        return (
            person('kanton_zug_demokratischer_freistaat', period) *
            person('kanton_zug_souveraenes_bundesglied', period) *
            ~person('zuger_kantonalsouveraenitaet_beschraenkt', period)
        )
