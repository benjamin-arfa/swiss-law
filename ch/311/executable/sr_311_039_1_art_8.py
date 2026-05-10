"""SR 311.039.1 Art. 8

Generated from: ch/311/de/311.039.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anrechenbare_ausgaben(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Ausgaben fuer die Massnahme (unmittelbar mit Vorbereitung und Durchfuehrung zusammenhaengend)"
    reference = "SR 311.039.1 Art. 8 Abs. 2"


class finanzhilfe_max_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstanteil der Finanzhilfe an den anrechenbaren Ausgaben (50%)"
    reference = "SR 311.039.1 Art. 8 Abs. 1"
    default_value = 0.5


class finanzhilfe_hoechstbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag der Finanzhilfe"
    reference = "SR 311.039.1 Art. 8"

    def formula(person, period, parameters):
        ausgaben = person('anrechenbare_ausgaben', period)
        return ausgaben * 0.5
