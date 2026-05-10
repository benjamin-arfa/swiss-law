"""SR 415.0 Art. 6

Generated from: ch/415/de/415.0.md

Jugend und Sport - Programm, Altersvoraussetzungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person (Kalenderjahr)"
    reference = "SR 415.0 Art. 6 Abs. 3"


# --- Computed variables ---

class jugend_und_sport_teilnahmeberechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung zur Teilnahme an Jugend und Sport"
    reference = "SR 415.0 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        alter = person('alter', period)
        return (alter >= 5) * (alter <= 20)
