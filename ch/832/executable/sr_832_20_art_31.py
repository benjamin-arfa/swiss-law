"""SR 832.20 Art. 31

Generated from: ch/832/de/832.20.md

Art. 31: Hoehe der Renten (Survivor pension amounts)
- Abs. 1: Survivor pensions as % of insured income:
  - Widows/widowers: 40%
  - Half-orphans: 15%
  - Full orphans: 25%
  - All survivors combined: max 70%
- Abs. 2: Divorced spouse: 20%, but max the owed maintenance contribution.
- Abs. 3: If widow/widower + children exceed 70%, they are proportionally
  reduced. If combined with divorced spouse pension exceeds 90%, proportional
  reduction applies.
- Abs. 4: Complementary pension if survivors also receive AHV/IV pensions =
  90% of insured income minus AHV/IV pensions, but max per Abs. 1.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uvg_anzahl_halbwaisen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl rentenberechtigte Halbwaisen"
    reference = "SR 832.20 Art. 31 Abs. 1"


class uvg_anzahl_vollwaisen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl rentenberechtigte Vollwaisen"
    reference = "SR 832.20 Art. 31 Abs. 1"


class uvg_hat_witwe_witwer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberlebender Ehegatte hat Rentenanspruch"
    reference = "SR 832.20 Art. 31 Abs. 1"


class uvg_unterhaltsbeitrag_geschieden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geschuldeter Unterhaltsbeitrag an geschiedenen Ehegatten (jaehrlich, CHF)"
    reference = "SR 832.20 Art. 31 Abs. 2"


class uvg_hinterlassenenrente_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtbetrag aller UVG-Hinterlassenenrenten (jaehrlich, CHF)"
    reference = "SR 832.20 Art. 31"

    def formula(person, period, parameters):
        verdienst = person('uvg_versicherter_verdienst', period)
        witwe = person('uvg_hat_witwe_witwer', period)
        halbwaisen = person('uvg_anzahl_halbwaisen', period)
        vollwaisen = person('uvg_anzahl_vollwaisen', period)
        unterhalt = person('uvg_unterhaltsbeitrag_geschieden', period)
        p = parameters(period).uvg

        # Individual pension components
        rente_witwe = witwe * verdienst * p.hinterlassenenrente_witwe
        rente_halb = halbwaisen * verdienst * p.hinterlassenenrente_halbwaise
        rente_voll = vollwaisen * verdienst * p.hinterlassenenrente_vollwaise

        # Subtotal for widow/widower + children (max 70%)
        subtotal = rente_witwe + rente_halb + rente_voll
        max_subtotal = verdienst * p.hinterlassenenrente_max
        subtotal_capped = min_(subtotal, max_subtotal)

        # Divorced spouse pension (max 20% or maintenance)
        rente_geschieden = min_(
            verdienst * p.hinterlassenenrente_geschieden,
            unterhalt
        )

        # Total (max 90% with divorced spouse)
        total = subtotal_capped + rente_geschieden
        max_total = verdienst * p.hinterlassenenrente_max_mit_geschieden
        return min_(total, max_total)
