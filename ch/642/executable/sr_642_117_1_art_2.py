"""SR 642.117.1 Art. 2

Generated from: ch/642/de/642.117.1.md

Art. 2: Measurement of income of natural persons
(Bemessung des Einkommens natuerlicher Personen)

Abs. 1: Taxable income is based on income actually earned during the
tax period (Art. 40 DBG).

Abs. 2: Deductions under Art. 33(1)(g), 33(1bis), 33(2), 33(3) and
Art. 35 DBG are granted proportionally to the duration of tax liability.

Abs. 3: For partial-year tax liability, regular income is annualized
(12 months) for rate-setting purposes. Non-regular income is added at
actual amount. Art. 37 and 38 DBG remain reserved.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ifd_dauer_steuerpflicht_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer der Steuerpflicht in Monaten waehrend der Steuerperiode"
    reference = "SR 642.117.1 Art. 2 Abs. 2, 3"
    default_value = 12


class ifd_regelmaessiges_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Regelmaessig fliessendes Einkommen waehrend der Steuerpflichtdauer (CHF)"
    reference = "SR 642.117.1 Art. 2 Abs. 3"


class ifd_unregelmaessiges_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Nicht regelmaessig fliessendes Einkommen (CHF)"
    reference = "SR 642.117.1 Art. 2 Abs. 3"
    default_value = 0


class ifd_satzbestimmendes_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Satzbestimmendes Einkommen bei unterjaehriger Steuerpflicht (CHF)"
    reference = "SR 642.117.1 Art. 2 Abs. 3"

    def formula(person, period, parameters):
        dauer = person('ifd_dauer_steuerpflicht_monate', period)
        regelmaessig = person('ifd_regelmaessiges_einkommen', period)
        unregelmaessig = person('ifd_unregelmaessiges_einkommen', period)

        # Annualize regular income, add non-regular at actual amount
        # If full year (12 months), no annualization needed
        annualisiert = where(
            dauer < 12,
            regelmaessig * 12 / max_(dauer, 1) + unregelmaessig,
            regelmaessig + unregelmaessig
        )
        return annualisiert


class ifd_abzuege_anteilig_faktor(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteiliger Faktor fuer Abzuege bei unterjaehriger Steuerpflicht"
    reference = "SR 642.117.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        dauer = person('ifd_dauer_steuerpflicht_monate', period)
        return dauer / 12
