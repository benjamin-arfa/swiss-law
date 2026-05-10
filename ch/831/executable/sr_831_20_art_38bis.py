"""SR 831.20 Art. 38bis

Generated from: ch/831/de/831.20.md

Art. 38bis: Kuerzung wegen Ueberversicherung - Reduction for over-insurance:
- Abs. 1: In derogation from Art. 69 Abs. 2-3 ATSG, child pensions are
  reduced insofar as they together with the parent's pension exceed 90%
  of the relevant average annual income for that pension.
- Abs. 2: The Federal Council sets a minimum amount.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_ueberversicherung_kinderrenten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Kinderrenten nach Kuerzung wegen Ueberversicherung "
        "(Art. 38bis IVG, CHF/Monat)"
    )
    reference = "SR 831.20 Art. 38bis Abs. 1"

    def formula(person, period, parameters):
        iv_rente = person('iv_rente_betrag', period)
        kinderrenten = person('iv_kinderrenten_total', period)
        massgebendes_einkommen = person('iv_rente_massgebendes_einkommen', period.this_year)

        # 90% threshold on monthly basis
        schwelle_monatlich = (massgebendes_einkommen / 12) * 0.90
        summe = iv_rente + kinderrenten

        # Reduce child pensions if sum exceeds 90% of relevant income
        ueberschuss = max_(summe - schwelle_monatlich, 0)
        kinderrenten_gekuerzt = max_(kinderrenten - ueberschuss, 0)

        return kinderrenten_gekuerzt
