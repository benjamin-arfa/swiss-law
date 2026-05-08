"""SR 832.20 Art. 20

Generated from: ch/832/de/832.20.md

Art. 20: Hoehe (Disability pension amount)
- Abs. 1: The disability pension is 80% of the insured income at full
  disability; for partial disability, it is reduced proportionally.
- Abs. 2: If the insured also receives an IV or AHV pension, a complementary
  pension is granted = 90% of insured income minus IV/AHV pension, but at
  most the amount per Abs. 1.
- Abs. 2ter: At reference age, the pension is reduced for each full year
  the insured was older than 45 at the time of accident:
  a. by 2 percentage points (max 40%) if IV degree >= 40%
  b. by 1 percentage point (max 20%) if IV degree < 40%
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uvg_iv_oder_ahv_rente(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der IV- oder AHV-Rente (jaehrlich, CHF)"
    reference = "SR 832.20 Art. 20 Abs. 2"


class uvg_alter_bei_unfall(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der versicherten Person zum Unfallzeitpunkt (Jahre)"
    reference = "SR 832.20 Art. 20 Abs. 2ter"


class uvg_hat_referenzalter_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat das Referenzalter erreicht"
    reference = "SR 832.20 Art. 20 Abs. 2ter"


class uvg_invalidenrente_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UVG-Invalidenrente (jaehrlich, CHF)"
    reference = "SR 832.20 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        verdienst = person('uvg_versicherter_verdienst', period)
        iv_grad = person('uvg_invaliditaetsgrad', period)
        p = parameters(period).uvg

        # Base pension: 80% of insured income * disability fraction
        rente = verdienst * p.invalidenrente_satz * (iv_grad / 100)
        return rente


class uvg_komplementaerrente_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UVG-Komplementaerrente (jaehrlich, CHF)"
    reference = "SR 832.20 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        verdienst = person('uvg_versicherter_verdienst', period)
        iv_grad = person('uvg_invaliditaetsgrad', period)
        iv_ahv_rente = person('uvg_iv_oder_ahv_rente', period)
        p = parameters(period).uvg

        # Maximum UVG pension (Art. 20 Abs. 1)
        max_rente = verdienst * p.invalidenrente_satz * (iv_grad / 100)

        # Complementary pension = 90% of insured income - IV/AHV pension
        komplement = verdienst * p.komplementaerrente_hoechstsatz - iv_ahv_rente

        # But at most the base pension amount
        komplement = min_(komplement, max_rente)
        return max_(komplement, 0)


class uvg_invalidenrente_kuerzung_referenzalter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kuerzung der UVG-Invalidenrente bei Referenzalter (Prozentpunkte)"
    reference = "SR 832.20 Art. 20 Abs. 2ter"

    def formula(person, period, parameters):
        alter_unfall = person('uvg_alter_bei_unfall', period)
        iv_grad = person('uvg_invaliditaetsgrad', period)
        ref_erreicht = person('uvg_hat_referenzalter_erreicht', period)
        p = parameters(period).uvg

        # Years over 45 at time of accident
        jahre_ueber_45 = max_(alter_unfall - p.kuerzung_alter_schwelle, 0)

        # Reduction depends on IV degree
        kuerzung_40_plus = min_(
            jahre_ueber_45 * p.kuerzung_invaliditaet_40_prozentpunkte,
            p.kuerzung_max_40_plus
        )
        kuerzung_unter_40 = min_(
            jahre_ueber_45 * p.kuerzung_invaliditaet_unter_40_prozentpunkte,
            p.kuerzung_max_unter_40
        )

        kuerzung = where(iv_grad >= 40, kuerzung_40_plus, kuerzung_unter_40)

        # Only applies when reference age is reached
        return ref_erreicht * kuerzung
