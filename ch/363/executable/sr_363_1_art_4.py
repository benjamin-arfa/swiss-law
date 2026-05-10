"""SR 363.1 Art. 4

Generated from: ch/363/de/363.1.md

Entzug der Anerkennung durch EJPD wenn Voraussetzungen nicht mehr erfuellt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class labor_anerkennung_entzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "EJPD entzieht die Anerkennung, da Labor die Voraussetzungen nicht mehr erfuellt"
    reference = "SR 363.1 Art. 4"

    def formula(person, period, parameters):
        berechtigt = person('labor_anerkennung_berechtigt', period)
        return not_(berechtigt)
