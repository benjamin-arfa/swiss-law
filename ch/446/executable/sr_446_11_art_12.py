"""SR 446.11 Art. 12

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class veranstaltung_regelmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veranstaltung wird von der Traegerschaft regelmaessig durchgefuehrt"
    reference = "SR 446.11 Art. 12 Abs. 1 Bst. a"


class veranstaltung_bildet_leitungsfunktion_aus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veranstaltung bildet Teilnehmer im Hinblick auf Leitungs-, Beratungs- und Betreuungsfunktion aus"
    reference = "SR 446.11 Art. 12 Abs. 1 Bst. a"


class veranstaltung_hebt_sich_ab(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veranstaltung hebt sich klar von allgemeinen statutarischen Taetigkeiten ab"
    reference = "SR 446.11 Art. 12 Abs. 1 Bst. b"


class bereits_durch_sportfoerderungsgesetz_unterstuetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aus-/Weiterbildung wird bereits durch Sportfoerderungsgesetz (SR 415.0) unterstuetzt"
    reference = "SR 446.11 Art. 12 Abs. 2"


class ist_aus_weiterbildung_kjfv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Qualifiziert als Aus- und Weiterbildung nach Art. 9 KJFG"
    reference = "SR 446.11 Art. 12"

    def formula(person, period, parameters):
        regelmaessig = person('veranstaltung_regelmaessig', period)
        leitungsfunktion = person('veranstaltung_bildet_leitungsfunktion_aus', period)
        hebt_ab = person('veranstaltung_hebt_sich_ab', period)
        sport = person('bereits_durch_sportfoerderungsgesetz_unterstuetzt', period)
        return regelmaessig * leitungsfunktion * hebt_ab * not_(sport)
