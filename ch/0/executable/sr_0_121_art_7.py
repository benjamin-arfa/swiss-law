"""SR 0.121 Art. VII

Generated from: ch/0/de/0.121.md

Inspection rights: Contracting Parties may designate observers for
inspections. Observers have free access to all areas of Antarctica.
All stations, equipment, ships, and aircraft are open to inspection.
Advance notification of expeditions, stations, and military movements.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class antarktis_recht_beobachter_ernennung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht zur Ernennung von Beobachtern fuer Inspektionen besteht"
    reference = "SR 0.121 Art. VII Abs. 1"


class antarktis_beobachter_freier_zugang(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Beobachter jederzeit freien Zugang zu allen Gebieten der Antarktis haben"
    reference = "SR 0.121 Art. VII Abs. 2"

    def formula(person, period, parameters):
        return person('antarktis_recht_beobachter_ernennung', period)


class antarktis_stationen_offen_inspektion(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Stationen und Einrichtungen zur Inspektion offenstehen"
    reference = "SR 0.121 Art. VII Abs. 3"

    def formula(person, period, parameters):
        return person('antarktis_vertrag_anwendbar', period)


class antarktis_vorherige_unterrichtung_expeditionen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vertragspartei die anderen Parteien vorab ueber Expeditionen unterrichtet"
    reference = "SR 0.121 Art. VII Abs. 5"
