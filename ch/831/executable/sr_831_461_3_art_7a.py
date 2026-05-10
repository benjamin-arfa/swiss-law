"""SR 831.461.3 Art. 7a

Generated from: ch/831/de/831.461.3.md

Additional buy-in contributions to pillar 3a (since 2025):
- Permitted if not all maximum contributions were made in the preceding 10 years
- Must have been entitled to contribute in the years being compensated
- Must make full regular contribution in the buy-in year
- Maximum buy-in: difference between sum of allowed and actually paid contributions
  over 10 years, but never more than 8% of upper BVG threshold
- Only one buy-in per gap year; one buy-in can cover multiple gap years
- No buy-in after first benefit withdrawal
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bvv3_einkauf_beitragslücke_10_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Summe der Beitragsluecken der letzten 10 Jahre (Differenz zwischen zulaessigen und geleisteten Beitraegen) in CHF"
    reference = "SR 831.461.3 Art. 7a Abs. 2"


class bvv3_einkauf_regulaerer_beitrag_geleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob im Einkaufsjahr der regulaere Beitrag nach Art. 7 Abs. 1 vollstaendig geleistet wurde"
    reference = "SR 831.461.3 Art. 7a Abs. 1 Bst. c"


class bvv3_altersleistung_bereits_bezogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob bereits eine Altersleistung nach Art. 3 Abs. 1 bezogen wurde"
    reference = "SR 831.461.3 Art. 7a Abs. 4"


class bvv3_einkauf_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person berechtigt ist, einen Einkauf in die Saeule 3a vorzunehmen"
    reference = "SR 831.461.3 Art. 7a Abs. 1"

    def formula_2025(person, period, parameters):
        luecke = person('bvv3_einkauf_beitragslücke_10_jahre', period)
        hat_luecke = luecke > 0
        beitrag_geleistet = person('bvv3_einkauf_regulaerer_beitrag_geleistet', period)
        bereits_bezogen = person('bvv3_altersleistung_bereits_bezogen', period)

        return hat_luecke * beitrag_geleistet * not_(bereits_bezogen)


class bvv3_einkauf_maximalbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Einkaufsbetrag in die Saeule 3a in CHF"
    reference = "SR 831.461.3 Art. 7a Abs. 2"

    def formula_2025(person, period, parameters):
        luecke = person('bvv3_einkauf_beitragslücke_10_jahre', period)
        grenzbetrag = person('bvv3_oberer_grenzbetrag_bvg', period)

        # Max 8% of upper BVG threshold
        obergrenze = grenzbetrag * 0.08

        berechtigt = person('bvv3_einkauf_berechtigt', period)

        return where(berechtigt, min_(luecke, obergrenze), 0.0)
