"""SR 142.318 Art. 10

Generated from: ch/142/de/142.318.md

Beschwerdefristen im beschleunigten Verfahren: Beschwerde gegen
Entscheid nach Art. 31a Abs. 4 AsylG innerhalb von 30 Tagen,
gegen Zwischenverfuegungen innerhalb von 10 Tagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_beschwerde_gegen_entscheid(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um eine Beschwerde gegen einen Entscheid nach Art. 31a Abs. 4 AsylG handelt"
    reference = "SR 142.318 Art. 10"


class ist_beschwerde_gegen_zwischenverfuegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um eine Beschwerde gegen eine Zwischenverfuegung handelt"
    reference = "SR 142.318 Art. 10"


class beschwerdefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Beschwerdefrist in Tagen im beschleunigten Verfahren"
    reference = "SR 142.318 Art. 10"

    def formula_2020_04(person, period, parameters):
        entscheid = person('ist_beschwerde_gegen_entscheid', period)
        zwischenverfuegung = person('ist_beschwerde_gegen_zwischenverfuegung', period)
        return where(
            entscheid,
            parameters(period).beschwerdefrist_entscheid_tage,
            where(
                zwischenverfuegung,
                parameters(period).beschwerdefrist_zwischenverfuegung_tage,
                0
            )
        )
