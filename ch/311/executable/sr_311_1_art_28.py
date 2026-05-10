"""SR 311.1 Art. 28

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class freiheitsentzug_dauer_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ausgesprochener Freiheitsentzug in Tagen"
    reference = "SR 311.1 Art. 28"


class freiheitsentzug_verbuesst_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Bereits verbuessste Tage des Freiheitsentzugs"
    reference = "SR 311.1 Art. 28"


class bedingte_entlassung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann der Jugendliche bedingt entlassen werden (Haelfte verbuesst, min. 14 Tage)"
    reference = "SR 311.1 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        dauer = person('freiheitsentzug_dauer_tage', period)
        verbuesst = person('freiheitsentzug_verbuesst_tage', period)
        haelfte = dauer / 2
        # Must have served at least half and at least 14 days
        return (verbuesst >= haelfte) * (verbuesst >= 14)
