"""SR 313.32 Art. 12

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schreibgebuehr_pro_seite(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schreibgebuehr pro Seite fuer die Herstellung des Originals (10 CHF)"
    reference = "SR 313.32 Art. 12 Abs. 1 lit. a"
    default_value = 10.0


class anzahl_seiten_original(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Seiten des Originals"
    reference = "SR 313.32 Art. 12"


class schreibgebuehr_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Totale Schreibgebuehr"
    reference = "SR 313.32 Art. 12"

    def formula(person, period, parameters):
        seiten = person('anzahl_seiten_original', period)
        return seiten * 10.0
