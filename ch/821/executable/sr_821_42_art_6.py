"""SR 821.42 Art. 6

Generated from: ch/821/de/821.42.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class friedenspflicht_aktiv(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Friedenspflicht besteht waehrend des Einigungs- oder Schiedsverfahrens "
        "(keine Kampfmassnahmen erlaubt)"
    )
    reference = "SR 821.42 Art. 6 Abs. 1"


class friedenspflicht_dauer_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Friedenspflicht in Tagen (Grundfrist: 45 Tage, verlaengerbar)"
    reference = "SR 821.42 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        # Art. 6 Abs. 1: Die Friedenspflicht dauert 45 Tage.
        # Durch einstimmigen Beschluss kann die Frist verlaengert werden.
        verlaengerung = person('friedenspflicht_verlaengerung_tage', period)
        return 45 + verlaengerung


class friedenspflicht_verlaengerung_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Verlaengerung der Friedenspflicht in Tagen (durch einstimmigen Beschluss)"
    reference = "SR 821.42 Art. 6 Abs. 1"
    default_value = 0


class friedenspflicht_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Friedenspflicht wurde verletzt"
    reference = "SR 821.42 Art. 6 Abs. 3"


class friedenspflicht_verletzung_veroeffentlicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verletzung der Friedenspflicht wird der Oeffentlichkeit bekanntgegeben "
        "(wenn fehlbare Partei von Verhalten nicht absteht)"
    )
    reference = "SR 821.42 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        verletzt = person('friedenspflicht_verletzt', period, options=[ADD])
        return verletzt > 0
