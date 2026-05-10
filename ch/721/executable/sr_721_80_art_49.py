"""SR 721.80 Art. 49

Generated from: ch/721/de/721.80.md

Art. 49 - Maximum water rate (Wasserzins):
1. The Wasserzins may not exceed CHF 110/year per kW gross capacity (until end of 2030).
   Of this, the Confederation may levy max CHF 1/kW for compensation payments
   under Art. 22(3)-(5).
2. Concession-based water power plants and their electricity may not be subject
   to special taxes, except where cantonal max Wasserzins is below the federal max.
4. Plants up to 1 MW gross capacity are exempt from Wasserzins.
   Between 1 and 2 MW, only a linear ramp-up to the maximum is permitted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wrg_wasserzins_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plant is exempt from Wasserzins (gross capacity <= 1 MW)"
    reference = "SR 721.80 Art. 49 Abs. 4"

    def formula(person, period, parameters):
        bruttoleistung_kw = person('wrg_bruttoleistung_kw', period)
        schwelle_mw = parameters(period).sr_721_80.wasserzins_befreiung_schwelle_mw
        return bruttoleistung_kw <= schwelle_mw * 1000


class wrg_wasserzins_effektiver_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Effective Wasserzins rate per kW considering linear ramp-up (CHF/kW/year)"
    reference = "SR 721.80 Art. 49 Abs. 1, 4"

    def formula(person, period, parameters):
        bruttoleistung_kw = person('wrg_bruttoleistung_kw', period)
        p = parameters(period).sr_721_80

        max_satz = p.wasserzins_maximum_pro_kw
        schwelle_kw = p.wasserzins_befreiung_schwelle_mw * 1000  # 1 MW = 1000 kW
        obergrenze_kw = p.wasserzins_linear_obergrenze_mw * 1000  # 2 MW = 2000 kW

        # Below threshold: exempt (0)
        # Between threshold and upper bound: linear ramp from 0 to max
        # Above upper bound: full max rate
        anteil = (bruttoleistung_kw - schwelle_kw) / (obergrenze_kw - schwelle_kw)
        anteil_begrenzt = min_(max_(anteil, 0), 1)

        return where(bruttoleistung_kw <= schwelle_kw, 0, anteil_begrenzt * max_satz)


class wrg_wasserzins_maximum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximum annual Wasserzins for the plant (CHF/year)"
    reference = "SR 721.80 Art. 49"

    def formula(person, period, parameters):
        bruttoleistung_kw = person('wrg_bruttoleistung_kw', period)
        effektiver_satz = person('wrg_wasserzins_effektiver_satz', period)

        return bruttoleistung_kw * effektiver_satz


class wrg_wasserzins_bundesanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximum federal share of Wasserzins for landscape compensation fund (CHF/year)"
    reference = "SR 721.80 Art. 49 Abs. 1"

    def formula(person, period, parameters):
        bruttoleistung_kw = person('wrg_bruttoleistung_kw', period)
        befreit = person('wrg_wasserzins_befreit', period)
        bundesanteil_satz = parameters(period).sr_721_80.wasserzins_bundesanteil_pro_kw

        return where(befreit, 0, bruttoleistung_kw * bundesanteil_satz)
