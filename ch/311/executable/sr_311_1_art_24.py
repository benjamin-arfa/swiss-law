"""SR 311.1 Art. 24

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class busse_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darf der Jugendliche mit Busse bestraft werden (ab 15 Jahren)"
    reference = "SR 311.1 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        return alter >= 15


class busse_hoechstbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag der Busse fuer Jugendliche (2000 CHF)"
    reference = "SR 311.1 Art. 24 Abs. 1"
    default_value = 2000.0


class busse_umwandlung_freiheitsentzug_max_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer des Freiheitsentzugs bei Umwandlung einer unbezahlten Busse (30 Tage)"
    reference = "SR 311.1 Art. 24 Abs. 5"
    default_value = 30
