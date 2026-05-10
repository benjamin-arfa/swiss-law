"""SR 831.30 Art. 9a

Generated from: ch/831/de/831.30.md

Art. 9a: Voraussetzungen hinsichtlich des Vermoegens (Wealth requirements)

Abs. 1: Entitlement to supplementary benefits requires net wealth below:
  a. Single persons: CHF 100,000
  b. Married couples: CHF 200,000
  c. Entitled orphans / children with AHV/IV child pension: CHF 50,000

Abs. 2: Owner-occupied property is excluded from net wealth calculation.
Abs. 3: Voluntarily relinquished assets (Art. 11a) count toward net wealth.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_ist_verheiratet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist verheiratet"
    reference = "SR 831.30 Art. 9a"


class el_ist_waise_oder_kind_mit_kinderrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist rentenberechtigte Waise oder Kind mit Kinderrente AHV/IV"
    reference = "SR 831.30 Art. 9a Abs. 1 Bst. c"


class el_reinvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reinvermoegen (ohne selbstbewohnte Liegenschaft, inkl. Vermoegensverzicht)"
    reference = "SR 831.30 Art. 9a"


class el_bewohnt_eigene_liegenschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bewohnt eine Liegenschaft im Eigentum"
    reference = "SR 831.30 Art. 9a Abs. 2"


class el_verzichtvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegen auf das verzichtet wurde (Art. 11a ELG)"
    reference = "SR 831.30 Art. 9a Abs. 3"


class el_vermoegensschwelle(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwendbare Vermoegensschwelle in CHF (Art. 9a ELG)"
    reference = "SR 831.30 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        ist_verheiratet = person('el_ist_verheiratet', period)
        ist_waise = person('el_ist_waise_oder_kind_mit_kinderrente', period)

        # a. Single: 100,000; b. Couple: 200,000; c. Orphan/child: 50,000
        return np.where(
            ist_waise, 50000.0,
            np.where(ist_verheiratet, 200000.0, 100000.0)
        )


class el_vermoegensvoraussetzung_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegensschwelle fuer EL-Anspruch nicht ueberschritten (Art. 9a ELG)"
    reference = "SR 831.30 Art. 9a"

    def formula(person, period, parameters):
        reinvermoegen = person('el_reinvermoegen', period)
        verzicht = person('el_verzichtvermoegen', period)
        schwelle = person('el_vermoegensschwelle', period)

        # Net wealth including relinquished assets must be below threshold
        gesamtvermoegen = reinvermoegen + verzicht
        return gesamtvermoegen < schwelle
