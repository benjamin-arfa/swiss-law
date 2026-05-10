"""SR 748.0 Art. 8

Generated from: ch/748/de/748.0.md

Art. 8: Flugplatzpflicht und Aussenlandungen
- Aircraft may only take off or land at aerodromes
- Federal Council regulates conditions for off-aerodrome operations
- Mountain landings for training/tourism only at designated sites
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lfg_ist_flugplatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Standort ist ein Flugplatz"
    reference = "SR 748.0 Art. 8 Abs. 1"


class lfg_aussenlandung_bewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Aussenlandung ist bewilligt (Art. 8 Abs. 2)"
    reference = "SR 748.0 Art. 8 Abs. 2"
    default_value = False


class lfg_ist_gebirgslandeplatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Standort ist ein bezeichneter Gebirgslandeplatz (Art. 8 Abs. 3)"
    reference = "SR 748.0 Art. 8 Abs. 3"


class lfg_abflug_landung_erlaubt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Abflug oder Landung am Standort ist erlaubt"
    reference = "SR 748.0 Art. 8"

    def formula(person, period, parameters):
        flugplatz = person('lfg_ist_flugplatz', period)
        aussenlandung = person('lfg_aussenlandung_bewilligt', period)
        gebirge = person('lfg_ist_gebirgslandeplatz', period)

        return (flugplatz + aussenlandung + gebirge) > 0
