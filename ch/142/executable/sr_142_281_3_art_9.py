"""SR 142.281.3 Art. 9

Generated from: ch/142/de/142.281.3.md

Korrektur der anerkannten Kosten bei Umbauten: Wenn Bereichsflaechen nicht
erreicht werden, werden die Bereichskosten im Verhaeltnis der fehlenden
Flaeche zur anrechenbaren Flaeche gekuerzt. Fehlende Flaeche im Bereich
Wohnen kann durch Mehr im Bereich Insassenwesen kompensiert werden
(Korrekturfaktor max. 1.15).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tatsaechliche_wohnflaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tatsaechliche Flaeche im Bereich Wohnen pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 9"


class tatsaechliche_insassenwesen_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tatsaechliche Flaeche im Bereich Insassenwesen pro Haftplatz (m2)"
    reference = "SR 142.281.3 Art. 9"


class korrektur_wohnen_durch_insassenwesen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Korrektur: Kompensation fehlender Wohnflaeche durch Insassenwesen-Mehrflaeche"
    reference = "SR 142.281.3 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        soll_wohnen = person('bereich_wohnen_flaeche', period)
        ist_wohnen = person('tatsaechliche_wohnflaeche', period)
        soll_insassen = person('bereich_insassenwesen_flaeche', period)
        ist_insassen = person('tatsaechliche_insassenwesen_flaeche', period)

        fehlend_wohnen = max_(soll_wohnen - ist_wohnen, 0)
        mehr_insassen = max_(ist_insassen - soll_insassen, 0)

        # Kompensation begrenzt auf fehlende Wohnflaeche
        kompensation = min_(fehlend_wohnen, mehr_insassen)

        # Korrekturfaktor Insassenwesen max. 1.15
        max_insassen_erhoehung = soll_insassen * 0.15
        kompensation = min_(kompensation, max_insassen_erhoehung)

        return kompensation
