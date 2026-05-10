"""SR 221.213.2 Art. 7

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pacht_ist_gewerbe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtgegenstand ist ein landwirtschaftliches Gewerbe (nicht Einzelgrundstück)"
    reference = "SR 221.213.2 Art. 7 Abs. 1"


class bewilligung_kuerzere_pachtdauer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Behördliche Bewilligung für kürzere Pachtdauer erteilt"
    reference = "SR 221.213.2 Art. 7 Abs. 2"


class vereinbarte_pachtdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vereinbarte Pachtdauer in Jahren"
    reference = "SR 221.213.2 Art. 7"


class mindestpachtdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesetzliche Mindestpachtdauer in Jahren"
    reference = "SR 221.213.2 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        ist_gewerbe = person('pacht_ist_gewerbe', period)
        # Gewerbe: mindestens 9 Jahre, Einzelgrundstücke: mindestens 6 Jahre
        return where(ist_gewerbe, 9, 6)


class gueltige_pachtdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gültige Pachtdauer in Jahren (unter Berücksichtigung der Mindestdauer)"
    reference = "SR 221.213.2 Art. 7"

    def formula(person, period, parameters):
        vereinbart = person('vereinbarte_pachtdauer_jahre', period)
        mindest = person('mindestpachtdauer_jahre', period)
        bewilligung = person('bewilligung_kuerzere_pachtdauer', period)
        # Kürzere Dauer nur mit Bewilligung gültig, sonst gilt Mindestdauer
        return where(bewilligung + (vereinbart >= mindest), vereinbart, mindest)
