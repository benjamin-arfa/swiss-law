"""SR 312.1 Art. 27

Generated from: ch/312/de/312.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class untersuchungshaft_verlaengerungsgesuch_frist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Verlaengerungsgesuch der Untersuchungshaft (7 Tage)"
    reference = "SR 312.1 Art. 27 Abs. 2"
    default_value = 7


class entscheid_frist_nach_gesuch_stunden(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Entscheid des Zwangsmassnahmengerichts nach Eingang des Gesuchs (48 Stunden)"
    reference = "SR 312.1 Art. 27 Abs. 2"
    default_value = 48


class untersuchungshaft_verlaengerung_max_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer jeder Verlaengerung der Untersuchungshaft (1 Monat)"
    reference = "SR 312.1 Art. 27 Abs. 3"
    default_value = 1
