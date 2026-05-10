"""SR 702.1 Art. 8

Generated from: ch/702/de/702.1.md

Sistierung nach Art. 14 Abs. 1 lit. a des Gesetzes:
Suspension of use restriction for max 2 years, exceptionally extendable by 2 more years.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sistierung_art14a_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer der Sistierung nach Art. 14 Abs. 1 lit. a in Jahren"
    reference = "SR 702.1 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return 2  # hoechstens zwei Jahre


class sistierung_art14a_verlaengerung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale ausnahmsweise Verlaengerung der Sistierung in Jahren"
    reference = "SR 702.1 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return 2  # um bis zu zwei Jahre


class sistierung_art14a_triftige_gruende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob triftige Gruende fuer eine Verlaengerung der Sistierung vorliegen"
    reference = "SR 702.1 Art. 8 Abs. 1"


class sistierung_art14a_max_gesamtdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Gesamtdauer der Sistierung nach Art. 14 Abs. 1 lit. a in Jahren"
    reference = "SR 702.1 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        basis = person('sistierung_art14a_dauer_jahre', period)
        verlaengerung = person('sistierung_art14a_verlaengerung_jahre', period)
        triftig = person('sistierung_art14a_triftige_gruende', period)
        return basis + where(triftig, verlaengerung, 0)
