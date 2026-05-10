"""SR 232.11 Art. 12

Generated from: ch/232/de/232.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class marke_letzte_benutzung_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der letzten Benutzung der Marke"
    reference = "SR 232.11 Art. 12 Abs. 1"


class widerspruchsfrist_abgelaufen_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr des Ablaufs der Widerspruchsfrist"
    reference = "SR 232.11 Art. 12 Abs. 1"


class wichtige_gruende_fuer_nichtgebrauch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wichtige Gründe für den Nichtgebrauch der Marke liegen vor"
    reference = "SR 232.11 Art. 12 Abs. 1"


class markenrecht_nicht_mehr_geltend_machbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Markenrecht kann wegen Nichtgebrauchs nicht mehr geltend gemacht werden"
    reference = "SR 232.11 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        letzte_benutzung = person('marke_letzte_benutzung_jahr', period)
        widerspruch_ablauf = person('widerspruchsfrist_abgelaufen_jahr', period)
        wichtige_gruende = person('wichtige_gruende_fuer_nichtgebrauch', period)
        aktuelles_jahr = period.start.year
        # 5 Jahre ununterbrochener Nichtgebrauch nach Ablauf der Widerspruchsfrist
        jahre_seit_ablauf = aktuelles_jahr - widerspruch_ablauf
        jahre_ohne_gebrauch = aktuelles_jahr - letzte_benutzung
        nichtgebrauch_5_jahre = (jahre_seit_ablauf > 5) * (jahre_ohne_gebrauch >= 5)
        return nichtgebrauch_5_jahre * not_(wichtige_gruende)
