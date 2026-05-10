"""SR 519.1 Art. 10

Generated from: ch/519/de/519.1.md

Art. 10 Funktionszulage (Function allowance):
1. A function allowance may be paid if a person fulfils tasks with special
   requirements without justifying a permanent reclassification.
2. The allowance is at most the difference between the maximum of the salary
   class per contract (or individual salary) and the maximum of the higher-rated
   function.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pvspa_erfuellt_besondere_anforderungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the person fulfils tasks with special requirements (besondere Anforderungen)"
    reference = "SR 519.1 Art. 10 Abs. 1"


class pvspa_hoechstbetrag_lohnklasse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximum amount of the salary class per employment contract (CHF)"
    reference = "SR 519.1 Art. 10 Abs. 2"


class pvspa_hoechstbetrag_hoehere_funktion(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximum amount of the higher-rated function (CHF)"
    reference = "SR 519.1 Art. 10 Abs. 2"


class pvspa_funktionszulage(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Function allowance amount (CHF), max = difference between higher function max and own salary class max"
    reference = "SR 519.1 Art. 10"

    def formula(person, period, parameters):
        besondere_anforderungen = person('pvspa_erfuellt_besondere_anforderungen', period)
        hoechstbetrag_lohnklasse = person('pvspa_hoechstbetrag_lohnklasse', period)
        hoechstbetrag_hoehere_funktion = person('pvspa_hoechstbetrag_hoehere_funktion', period)

        max_zulage = max_(hoechstbetrag_hoehere_funktion - hoechstbetrag_lohnklasse, 0)
        return where(besondere_anforderungen, max_zulage, 0)
