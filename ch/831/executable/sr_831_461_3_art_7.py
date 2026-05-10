"""SR 831.461.3 Art. 7

Generated from: ch/831/de/831.461.3.md

Tax-deductible contributions to recognized pension plans (pillar 3a / BVV 3):
- Employees/self-employed with 2nd pillar: up to 8% of the upper threshold
  amount per Art. 8(1) BVG
- Employees/self-employed without 2nd pillar: up to 20% of earned income,
  max 40% of upper threshold amount per Art. 8(1) BVG
- Both spouses/partners can claim deductions if both are employed
- Contributions may be made up to 5 years after reaching reference age
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bvv3_angehoerigkeit_vorsorgeeinrichtung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einer Vorsorgeeinrichtung nach Art. 80 BVG (2. Saeule) angehoert"
    reference = "SR 831.461.3 Art. 7 Abs. 1"


class bvv3_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erwerbseinkommen der Person (CHF)"
    reference = "SR 831.461.3 Art. 7 Abs. 1 Bst. b"


class bvv3_oberer_grenzbetrag_bvg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    default_value = 88200.0
    label = "Oberer Grenzbetrag nach Art. 8 Abs. 1 BVG (CHF)"
    reference = "SR 831.461.3 Art. 7 Abs. 1"


class bvv3_maximaler_abzug(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler steuerlicher Abzug fuer Beitraege an die gebundene Selbstvorsorge (Saeule 3a) in CHF"
    reference = "SR 831.461.3 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        hat_2_saeule = person('bvv3_angehoerigkeit_vorsorgeeinrichtung', period)
        einkommen = person('bvv3_erwerbseinkommen', period)
        grenzbetrag = person('bvv3_oberer_grenzbetrag_bvg', period)

        # With 2nd pillar: 8% of upper threshold (small 3a)
        abzug_mit = grenzbetrag * 0.08

        # Without 2nd pillar: 20% of income, max 40% of upper threshold (large 3a)
        abzug_ohne_max = grenzbetrag * 0.40
        abzug_ohne = min_(einkommen * 0.20, abzug_ohne_max)

        return where(hat_2_saeule, abzug_mit, abzug_ohne)


class bvv3_geleistete_beitraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tatsaechlich geleistete Beitraege an die gebundene Selbstvorsorge (Saeule 3a) in CHF"
    reference = "SR 831.461.3 Art. 7"


class bvv3_steuerlich_abzugsfaehiger_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerlich abzugsfaehiger Betrag der Saeule-3a-Beitraege in CHF"
    reference = "SR 831.461.3 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        geleistet = person('bvv3_geleistete_beitraege', period)
        maximum = person('bvv3_maximaler_abzug', period)
        return min_(geleistet, maximum)
