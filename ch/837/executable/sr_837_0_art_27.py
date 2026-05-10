"""SR 837.0 Art. 27

Generated from: ch/837/de/837.0.md

Art. 27: Hoechstzahl der Taggelder (Maximum number of daily allowances)
- Abs. 2: The insured person is entitled to:
  a. max 260 daily allowances for 12 months of contributions
  b. max 400 daily allowances for 18 months of contributions
  c. max 520 daily allowances for 22+ months contributions AND either:
     1. has reached 55 years of age, or
     2. receives IV pension corresponding to at least 40% disability
- Abs. 4: Persons exempt from contribution period: max 90 daily allowances
- Abs. 5: Persons after loss of IV pension: max 180 daily allowances
- Abs. 5bis: Persons under 25 without child support: max 200 daily allowances
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der versicherten Person in Jahren"
    reference = "SR 837.0 Art. 27"


class alv_iv_rente_wegfall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Rente ist weggefallen und Person muss unselbstaendige Erwerbstaetigkeit aufnehmen"
    reference = "SR 837.0 Art. 27 Abs. 5"


class alv_hoechstzahl_taggelder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstzahl der Taggelder innerhalb der Rahmenfrist"
    reference = "SR 837.0 Art. 27"

    def formula(person, period, parameters):
        beitragszeit = person('alv_beitragszeit_monate', period)
        befreit = person('alv_von_beitragszeit_befreit', period)
        alter = person('alv_alter', period)
        iv_rente_40 = person('alv_bezieht_iv_rente_40_prozent', period.first_month)
        iv_wegfall = person('alv_iv_rente_wegfall', period)
        unterhalt = person('alv_unterhaltspflicht_kinder_unter_25', period.first_month)
        p = parameters(period).alv

        # Art. 27 Abs. 5: persons after IV pension loss
        ist_iv_wegfall = iv_wegfall

        # Art. 27 Abs. 5bis: under 25 without child support
        ist_unter_25 = (alter < 25) * (unterhalt == False)

        # Art. 27 Abs. 4: exempt from contribution period
        ist_befreit = befreit * (ist_iv_wegfall == False)

        # Art. 27 Abs. 2c: 22+ months AND (55+ or IV >= 40%)
        hat_520 = (
            (beitragszeit >= 22)
            * ((alter >= p.alter_55_erhoehte_taggelder) + iv_rente_40)
        )

        # Art. 27 Abs. 2b: 18+ months
        hat_400 = (beitragszeit >= 18) * (hat_520 == False)

        # Art. 27 Abs. 2a: 12+ months (default for fulfilled contribution)
        hat_260 = (beitragszeit >= 12) * (hat_400 == False) * (hat_520 == False)

        hoechstzahl = (
            ist_iv_wegfall * p.hoechstzahl_taggelder_iv_wegfall
            + ist_unter_25 * (ist_iv_wegfall == False) * p.hoechstzahl_taggelder_unter_25
            + ist_befreit * (ist_unter_25 == False) * p.hoechstzahl_taggelder_befreit
            + (ist_iv_wegfall == False) * (ist_unter_25 == False) * (ist_befreit == False) * (
                hat_520 * p.hoechstzahl_taggelder_22_monate
                + hat_400 * p.hoechstzahl_taggelder_18_monate
                + hat_260 * p.hoechstzahl_taggelder_12_monate
            )
        )

        return hoechstzahl
