"""SR 171.13 Art. 33c

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindestredezeit_fraktion_legislaturplanung_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindest-Redezeit jeder Fraktion bei der Legislaturplanung in Minuten"
    reference = "SR 171.13 Art. 33c Abs. 3"

    def formula(person, period, parameters):
        return 10
