"""SR 220 Art. 21

Generated from: ch/de/220.md

Uebervorteilung: Bei offenbarem Missverhaeltnis zwischen Leistung und
Gegenleistung durch Ausbeutung der Notlage, Unerfahrenheit oder des
Leichtsinns kann der Verletzte innerhalb Jahresfrist erklaeren, dass er
den Vertrag nicht halte.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liegt_uebervorteilung_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Uebervorteilung nach Art. 21 OR vorliegt"
    reference = "SR 220 Art. 21"

    def formula(person, period, parameters):
        offenbares_missverhaeltnis = person('offenbares_missverhaeltnis_leistungen', period)
        ausbeutung_notlage = person('ausbeutung_notlage', period)
        ausbeutung_unerfahrenheit = person('ausbeutung_unerfahrenheit', period)
        ausbeutung_leichtsinn = person('ausbeutung_leichtsinn', period)

        ausbeutung = (ausbeutung_notlage + ausbeutung_unerfahrenheit + ausbeutung_leichtsinn) > 0
        return offenbares_missverhaeltnis * ausbeutung


class kann_uebervorteilung_geltend_machen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Verletzte die Uebervorteilung noch geltend machen kann (Jahresfrist)"
    reference = "SR 220 Art. 21 Abs. 1"

    def formula(person, period, parameters):
        liegt_vor = person('liegt_uebervorteilung_vor', period)
        monate_seit_vertragsschluss = person('monate_seit_vertragsschluss', period)
        frist = parameters(period).or_vertragsrecht.uebervorteilung.anfechtungsfrist_monate
        return liegt_vor * (monate_seit_vertragsschluss <= frist)


class offenbares_missverhaeltnis_leistungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein offenbares Missverhaeltnis zwischen Leistung und Gegenleistung besteht"
    reference = "SR 220 Art. 21 Abs. 1"


class ausbeutung_notlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ausbeutung der Notlage"
    reference = "SR 220 Art. 21 Abs. 1"


class ausbeutung_unerfahrenheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ausbeutung der Unerfahrenheit"
    reference = "SR 220 Art. 21 Abs. 1"


class ausbeutung_leichtsinn(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ausbeutung des Leichtsinns"
    reference = "SR 220 Art. 21 Abs. 1"


class monate_seit_vertragsschluss(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit Vertragsschluss"
    reference = "SR 220 Art. 21 Abs. 2"
