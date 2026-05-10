"""SR 415.0 Art. 25a

Generated from: ch/415/de/415.0.md

Strafbestimmung Wettkampfmanipulation - Freiheitsstrafe bis 3 Jahre, schwere Faelle bis 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class indirekte_wettkampfmanipulation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Indirekte Wettkampfmanipulation (Vorteil anbieten/versprechen/gewaehren)"
    reference = "SR 415.0 Art. 25a Abs. 1"


class direkte_wettkampfmanipulation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Direkte Wettkampfmanipulation (Vorteil fordern/annehmen)"
    reference = "SR 415.0 Art. 25a Abs. 2"


class wettkampfmanipulation_schwerer_fall(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwerer Fall Wettkampfmanipulation (Bande oder gewerbsmaessig)"
    reference = "SR 415.0 Art. 25a Abs. 3"


# --- Computed variables ---

class wettkampfmanipulation_strafbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafbarkeit wegen Wettkampfmanipulation"
    reference = "SR 415.0 Art. 25a"

    def formula(person, period, parameters):
        indirekt = person('indirekte_wettkampfmanipulation', period)
        direkt = person('direkte_wettkampfmanipulation', period)
        return indirekt + direkt


class wettkampfmanipulation_hoechststrafe_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechststrafe Freiheitsstrafe in Jahren bei Wettkampfmanipulation"
    reference = "SR 415.0 Art. 25a Abs. 1-3"

    def formula(person, period, parameters):
        strafbar = person('wettkampfmanipulation_strafbar', period)
        schwer = person('wettkampfmanipulation_schwerer_fall', period)
        return where(strafbar, where(schwer, 5, 3), 0)
