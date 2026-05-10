"""SR 642.21 Art. 8 - Ausnahmen bei Versicherungsleistungen (Insurance Exemptions)

Generated from: ch/642/de/642.21.md

Art. 8 Abs. 1: Exempt from withholding tax on insurance benefits:
  a) Capital benefits if total amount from the same insurance <= CHF 5,000
  b) Annuities/pensions if annual amount incl. supplements <= CHF 500
  c) Benefits under AHVG (SR 831.10) and IVG (SR 831.20)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vstg_versicherung_kapitalleistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalleistung aus derselben Versicherung (CHF)"
    reference = "SR 642.21 Art. 8 Abs. 1 Bst. a"
    default_value = 0.0


class vstg_versicherung_rente_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Renten und Pensionen einschliesslich Zulagen (CHF)"
    reference = "SR 642.21 Art. 8 Abs. 1 Bst. b"
    default_value = 0.0


class vstg_leistung_ahv_iv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Leistung auf der AHV (SR 831.10) oder IV (SR 831.20) beruht"
    reference = "SR 642.21 Art. 8 Abs. 1 Bst. c"


class vstg_kapitalleistung_steuerfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kapitalleistung von der Verrechnungssteuer befreit ist (<= CHF 5000)"
    reference = "SR 642.21 Art. 8 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        kapital = person('vstg_versicherung_kapitalleistung', period)
        schwelle = parameters(period).sr_642_21.kapitalleistung_freigrenze
        return kapital <= schwelle


class vstg_rente_steuerfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Renten/Pensionen von der Verrechnungssteuer befreit sind (<= CHF 500/Jahr)"
    reference = "SR 642.21 Art. 8 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        rente = person('vstg_versicherung_rente_jaehrlich', period)
        schwelle = parameters(period).sr_642_21.rente_freigrenze
        return rente <= schwelle


class vstg_versicherung_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Versicherungsleistung insgesamt von der Verrechnungssteuer befreit ist"
    reference = "SR 642.21 Art. 8"

    def formula(person, period, parameters):
        kapital_frei = person('vstg_kapitalleistung_steuerfrei', period)
        rente_frei = person('vstg_rente_steuerfrei', period)
        ahv_iv = person('vstg_leistung_ahv_iv', period)
        return kapital_frei + rente_frei + ahv_iv
