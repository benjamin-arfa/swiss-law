"""SR 514.54 Art. 4

Generated from: ch/514/de/514.54.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class druckluft_co2_muendungsenergie_joule(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Muendungsenergie der Druckluft-/CO2-Waffe in Joule"


class ist_druckluft_co2_waffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gegenstand ist eine Druckluft- oder CO2-Waffe"


class sieht_aus_wie_echte_feuerwaffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gegenstand kann mit echter Feuerwaffe verwechselt werden"


class druckluft_co2_gilt_als_waffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Druckluft-/CO2-Waffe gilt als Waffe im Sinne des WG (Art. 4 Abs. 1 lit. f SR 514.54)"
    reference = "SR 514.54 Art. 4"

    def formula(person, period, parameters):
        ist_dl = person('ist_druckluft_co2_waffe', period)
        energie = person('druckluft_co2_muendungsenergie_joule', period)
        verwechselbar = person('sieht_aus_wie_echte_feuerwaffe', period)
        # Mindestens 7.5 Joule ODER aufgrund Aussehen verwechselbar
        return ist_dl * ((energie >= 7.5) + verwechselbar)


class ladevorrichtung_kapazitaet(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kapazitaet der Ladevorrichtung in Patronen"


class ist_faustfeuerwaffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffe ist eine Faustfeuerwaffe"


class ist_handfeuerwaffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffe ist eine Handfeuerwaffe (keine Faustfeuerwaffe)"


class ladevorrichtung_hohe_kapazitaet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ladevorrichtung hat hohe Kapazitaet (Art. 4 Abs. 2bis SR 514.54)"
    reference = "SR 514.54 Art. 4"

    def formula(person, period, parameters):
        kapazitaet = person('ladevorrichtung_kapazitaet', period)
        faustfeuerwaffe = person('ist_faustfeuerwaffe', period)
        handfeuerwaffe = person('ist_handfeuerwaffe', period)
        # Faustfeuerwaffen: mehr als 20 Patronen
        # Handfeuerwaffen: mehr als 10 Patronen
        hohe_kap_faust = faustfeuerwaffe * (kapazitaet > 20)
        hohe_kap_hand = handfeuerwaffe * (kapazitaet > 10)
        return hohe_kap_faust + hohe_kap_hand
