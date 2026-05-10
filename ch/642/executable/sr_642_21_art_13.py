"""SR 642.21 Art. 13 - Steuersaetze (Tax Rates)

Generated from: ch/642/de/642.21.md

Art. 13 Abs. 1: The withholding tax rates are:
  a) On capital income, gambling winnings, lottery/skill-game winnings:
     35% of the taxable benefit
  b) On annuities (Leibrenten) and pensions: 15% of the taxable benefit
  c) On other insurance benefits: 8% of the taxable benefit

Art. 13 Abs. 2: The Federal Council may reduce the rate in lit. a
to 30% at year-end if monetary or capital market conditions require it.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vstg_steuer_kapitalertrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verrechnungssteuer auf Kapitalertraegen und Spielgewinnen (CHF)"
    reference = "SR 642.21 Art. 13 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        kapital = person('vstg_ertrag_bewegliches_kapitalvermoegen', period)
        geldspiele = person('vstg_gewinn_geldspiele', period)
        lotterien = person('vstg_gewinn_lotterien', period)
        p = parameters(period).sr_642_21
        return (kapital + geldspiele + lotterien) * p.steuersatz_kapitalertrag


class vstg_steuer_leibrenten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verrechnungssteuer auf Leibrenten und Pensionen (CHF)"
    reference = "SR 642.21 Art. 13 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        renten = person('vstg_versicherung_rente_jaehrlich', period)
        rente_frei = person('vstg_rente_steuerfrei', period)
        p = parameters(period).sr_642_21
        # Only taxable if above exemption threshold (Art. 8)
        return where(rente_frei, 0, renten * p.steuersatz_leibrenten)


class vstg_steuer_versicherung_sonstige(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verrechnungssteuer auf sonstigen Versicherungsleistungen (CHF)"
    reference = "SR 642.21 Art. 13 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        leistung = person('vstg_versicherungsleistung', period)
        befreit = person('vstg_versicherung_befreit', period)
        p = parameters(period).sr_642_21
        return where(befreit, 0, leistung * p.steuersatz_versicherung_sonstige)


class vstg_steuer_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte geschuldete Verrechnungssteuer (CHF)"
    reference = "SR 642.21 Art. 13"

    def formula(person, period, parameters):
        kapital = person('vstg_steuer_kapitalertrag', period)
        renten = person('vstg_steuer_leibrenten', period)
        versicherung = person('vstg_steuer_versicherung_sonstige', period)
        return kapital + renten + versicherung
