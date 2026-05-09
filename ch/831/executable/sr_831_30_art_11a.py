"""SR 831.30 Art. 11a

Generated from: ch/831/de/831.30.md

Art. 11a: Verzicht auf Einkuenfte und Vermoegenswerte - Renunciation of
income and assets (EL Reform 2021):

Abs. 1: Voluntary renunciation of reasonable employment -> hypothetical
income is counted.
Abs. 2: Other income/assets renounced without legal obligation and without
equivalent consideration are counted as if never renounced.
Abs. 3: Excessive asset depletion (>10% per year from entitlement to
survivor/IV pension, or >CHF 10,000 for assets up to CHF 100,000)
is treated as asset renunciation.
Abs. 4: For old-age pension recipients, Abs. 3 also applies to the 10
years before pension entitlement began.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_hypothetisches_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hypothetisches Erwerbseinkommen bei Verzicht auf zumutbare Erwerbstaetigkeit (Art. 11a Abs. 1 ELG)"
    reference = "SR 831.30 Art. 11a Abs. 1"


class el_verzichtetes_vermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verzichtete Vermoegenswerte (Art. 11a Abs. 2 ELG)"
    reference = "SR 831.30 Art. 11a Abs. 2"


class el_vermoegen_vorjahr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegen im Vorjahr"
    reference = "SR 831.30 Art. 11a Abs. 3"


class el_vermoegensverzicht_uebermass(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Uebermassiger Vermoegensverzehr als anrechenbarer Verzicht (Art. 11a Abs. 3 ELG)"
    reference = "SR 831.30 Art. 11a Abs. 3"

    def formula(person, period, parameters):
        vermoegen_aktuell = person('el_reinvermoegen', period)
        vermoegen_vorjahr = person('el_vermoegen_vorjahr', period)

        verbrauch = max_(vermoegen_vorjahr - vermoegen_aktuell, 0)

        # Allowed depletion: 10% of prior year assets, but at least CHF 10,000
        # for assets up to CHF 100,000
        grenze_prozent = vermoegen_vorjahr * 0.10
        grenze = where(vermoegen_vorjahr <= 100000, max_(grenze_prozent, 10000), grenze_prozent)

        # Excess depletion counted as renounced assets
        return max_(verbrauch - grenze, 0)
