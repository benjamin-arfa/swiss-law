"""SR 830.1 Art. 17

Generated from: ch/830/de/830.1.md

Art. 17: Revision der Invalidenrente und anderer Dauerleistungen.
Abs. 1: Rente wird erhöht/herabgesetzt/aufgehoben wenn Invaliditätsgrad
sich um mindestens 5 Prozentpunkte ändert oder auf 100% erhöht.
Abs. 2: Andere Dauerleistungen bei erheblicher Sachverhaltsänderung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bisheriger_invaliditaetsgrad(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bisheriger Invaliditätsgrad der Rentenbezügerin/des Rentenbezügers"
    reference = "SR 830.1 Art. 17 Abs. 1"


class neuer_invaliditaetsgrad(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Neuer Invaliditätsgrad nach Revision"
    reference = "SR 830.1 Art. 17 Abs. 1"


class rentenrevision_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Revision der Invalidenrente ist erforderlich: Änderung um mindestens "
        "5 Prozentpunkte oder Erhöhung auf 100% (Art. 17 Abs. 1 ATSG)"
    )
    reference = "SR 830.1 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        bisherig = person('bisheriger_invaliditaetsgrad', period)
        neu = person('neuer_invaliditaetsgrad', period)
        # lit. a: Änderung um mindestens 5 Prozentpunkte
        aenderung = abs_(neu - bisherig)
        mindestens_5pp = aenderung >= 0.05
        # lit. b: Erhöhung auf 100%
        auf_100 = neu >= 1.0
        return mindestens_5pp + auf_100 > 0
