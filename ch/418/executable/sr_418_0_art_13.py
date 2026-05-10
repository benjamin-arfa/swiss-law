"""SR 418.0 Art. 13

Generated from: ch/418/de/418.0.md

Entzug der Anerkennung, Auflagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class voraussetzungen_art_3_nicht_mehr_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen nach Art. 3 nicht mehr erfuellt"
    reference = "SR 418.0 Art. 13 Abs. 1"


class begruendete_aussicht_auf_wiederherstellung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Begruendete Aussichten, dass Voraussetzungen in absehbarer Zeit wieder erfuellt"
    reference = "SR 418.0 Art. 13 Abs. 1"


class anerkennung_entzogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anerkennung wird entzogen"
    reference = "SR 418.0 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        nicht_erfuellt = person('voraussetzungen_art_3_nicht_mehr_erfuellt', period)
        aussicht = person('begruendete_aussicht_auf_wiederherstellung', period)
        return nicht_erfuellt * not_(aussicht)
