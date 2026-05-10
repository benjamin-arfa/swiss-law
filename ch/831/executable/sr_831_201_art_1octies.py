"""SR 831.201 Art. 1octies

Generated from: ch/831/de/831.201.md

Hoechstbetrag fuer Massnahmen der Fruehintervention:
Die Kosten duerfen pro versicherte Person CHF 20,000 nicht uebersteigen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_kosten_fruehintervention(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bisherige Kosten fuer Massnahmen der Fruehintervention in Franken"
    reference = "SR 831.201 Art. 1octies"


class iv_fruehintervention_hoechstbetrag_ueberschritten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Hoechstbetrag fuer Fruehintervention (CHF 20'000) ueberschritten ist"
    reference = "SR 831.201 Art. 1octies"

    def formula(person, period, parameters):
        kosten = person('iv_kosten_fruehintervention', period)
        return kosten > 20_000


class iv_fruehintervention_restbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verbleibender Betrag fuer Massnahmen der Fruehintervention in Franken"
    reference = "SR 831.201 Art. 1octies"

    def formula(person, period, parameters):
        import numpy as np
        kosten = person('iv_kosten_fruehintervention', period)
        return np.maximum(20_000 - kosten, 0)
