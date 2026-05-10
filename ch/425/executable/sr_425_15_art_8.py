"""SR 425.15 Art. 8

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dienstleistung_besondere_schwierigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dienstleistung von besonderer Schwierigkeit"
    reference = "SR 425.15 Art. 8 lit. a"


class dienstleistung_dringlich_oder_ausserhalb_arbeitszeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dienstleistung dringlich oder ausserhalb der normalen Arbeitszeit"
    reference = "SR 425.15 Art. 8 lit. b"


class gebuehrenzuschlag_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gebuehrenzuschlag von hoechstens 50% ist anwendbar"
    reference = "SR 425.15 Art. 8"

    def formula(person, period, parameters):
        schwierig = person('dienstleistung_besondere_schwierigkeit', period)
        dringlich = person('dienstleistung_dringlich_oder_ausserhalb_arbeitszeit', period)
        return schwierig + dringlich


class maximaler_gebuehrenzuschlag_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Gebuehrenzuschlag in Prozent"
    reference = "SR 425.15 Art. 8"

    def formula(person, period, parameters):
        berechtigt = person('gebuehrenzuschlag_berechtigt', period)
        return where(berechtigt, 50.0, 0.0)
