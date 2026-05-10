"""SR 415.0 Art. 22

Generated from: ch/415/de/415.0.md

Strafbestimmungen Doping - Freiheitsstrafe bis 3 Jahre, in schweren Faellen bis 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class doping_handlung_nach_art_19_abs_3(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Dopingmittel hergestellt, erworben, eingefuehrt, vertrieben etc. zu Dopingzwecken"
    reference = "SR 415.0 Art. 22 Abs. 1"


class doping_schwerer_fall(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwerer Fall (Bande, Gesundheitsgefaehrdung, Minderjaeherige, gewerbsmaessig)"
    reference = "SR 415.0 Art. 22 Abs. 3"


class doping_nur_eigenkonsum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Herstellung/Erwerb/Besitz ausschliesslich zum eigenen Konsum"
    reference = "SR 415.0 Art. 22 Abs. 4"


# --- Computed variables ---

class doping_strafbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafbarkeit wegen Dopinghandlung"
    reference = "SR 415.0 Art. 22"

    def formula(person, period, parameters):
        handlung = person('doping_handlung_nach_art_19_abs_3', period)
        eigenkonsum = person('doping_nur_eigenkonsum', period)
        return handlung * not_(eigenkonsum)


class doping_hoechststrafe_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechststrafe Freiheitsstrafe in Jahren"
    reference = "SR 415.0 Art. 22 Abs. 1-2"

    def formula(person, period, parameters):
        strafbar = person('doping_strafbar', period)
        schwerer_fall = person('doping_schwerer_fall', period)
        return where(strafbar, where(schwerer_fall, 5, 3), 0)
