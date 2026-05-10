"""SR 642.11 Art. 22

Generated from: ch/642/de/642.11.md

Art. 22 Einkuenfte aus Vorsorge (Pension/retirement income):
1. Taxable are all income from AHV/IV (old age, survivors, disability
   insurance), occupational pension schemes (BVG), and recognized forms
   of tied individual provision (Saeule 3a), including capital payments
   and repayments of contributions.
2. Income from occupational pension includes benefits from pension funds,
   savings and group insurance, and vested benefits policies.
3. Life annuity insurance and life annuity/maintenance contracts are
   taxable at their yield portion (Ertragsanteil):
   a. Guaranteed benefits under VVG: yield based on max technical interest rate
   b. Surplus benefits under VVG: yield portion = 70%
   c. Foreign life annuities and maintenance contracts: yield based on
      10-year federal bond return + 0.5 percentage points
4. Art. 24 lit. b remains reserved (tax-free capital from private
   life insurance).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einkommen_ahv_iv_renten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Renten und Leistungen aus AHV/IV (CHF)"
    reference = "SR 642.11 Art. 22 Abs. 1"


class einkommen_berufliche_vorsorge(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus beruflicher Vorsorge (BVG, Pensionskasse, CHF)"
    reference = "SR 642.11 Art. 22 Abs. 1, 2"


class einkommen_gebundene_selbstvorsorge(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus gebundener Selbstvorsorge (Saeule 3a, CHF)"
    reference = "SR 642.11 Art. 22 Abs. 1"


class kapitalabfindung_vorsorge_rueckzahlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalabfindungen und Rueckzahlungen von Einlagen/Praemien/Beitraegen aus Vorsorge (CHF)"
    reference = "SR 642.11 Art. 22 Abs. 1"


class leibrente_jahresleistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahresleistung aus Leibrentenversicherung (CHF)"
    reference = "SR 642.11 Art. 22 Abs. 3"


class leibrente_technischer_zinssatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler technischer Zinssatz der Leibrentenversicherung (Rate)"
    reference = "SR 642.11 Art. 22 Abs. 3 Bst. a"


class leibrente_ist_vvg_garantiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Leibrente ist garantierte Leistung unter VVG (Art. 22 Abs. 3 Bst. a)"
    reference = "SR 642.11 Art. 22 Abs. 3 Bst. a"


class leibrente_ist_vvg_ueberschuss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Leibrente ist Ueberschussleistung unter VVG (Art. 22 Abs. 3 Bst. b)"
    reference = "SR 642.11 Art. 22 Abs. 3 Bst. b"


class leibrente_ertragsanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ertragsanteil der Leibrente (Rate, 0-1)"
    reference = "SR 642.11 Art. 22 Abs. 3"

    def formula(person, period, parameters):
        import numpy as np
        ist_vvg_garantiert = person('leibrente_ist_vvg_garantiert', period)
        ist_vvg_ueberschuss = person('leibrente_ist_vvg_ueberschuss', period)
        zinssatz = person('leibrente_technischer_zinssatz', period)

        # Art. 22 Abs. 3 Bst. a: Formel fuer garantierte VVG-Leistungen
        # Ertragsanteil = 40% * technischer Zinssatz / max(technischer Zinssatz, 0.5%)
        # Vereinfacht: wenn Zinssatz > 0 -> Berechnung; sonst 0%
        ertragsanteil_garantiert = where(
            zinssatz > 0,
            np.round(40 * zinssatz / max_(zinssatz, 0.005)) / 100,
            0
        )

        # Art. 22 Abs. 3 Bst. b: Ueberschussleistungen = 70%
        ertragsanteil_ueberschuss = 0.70

        # Art. 22 Abs. 3 Bst. c: Auslaendische Leibrenten (Restfall)
        # Vereinfachung: wenn weder a noch b, Ertragsanteil = 0 (benoetigt Bundesobligation-Rendite)
        ertragsanteil_auslaendisch = 0.0

        ertragsanteil = where(
            ist_vvg_garantiert,
            ertragsanteil_garantiert,
            where(ist_vvg_ueberschuss,
                   ertragsanteil_ueberschuss,
                   ertragsanteil_auslaendisch)
        )

        return ertragsanteil


class leibrente_steuerbarer_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbarer Betrag der Leibrente (CHF)"
    reference = "SR 642.11 Art. 22 Abs. 3"

    def formula(person, period, parameters):
        jahresleistung = person('leibrente_jahresleistung', period)
        ertragsanteil = person('leibrente_ertragsanteil', period)
        return jahresleistung * ertragsanteil


class einkommen_vorsorge_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte steuerbare Einkuenfte aus Vorsorge (CHF)"
    reference = "SR 642.11 Art. 22"

    def formula(person, period, parameters):
        ahv_iv = person('einkommen_ahv_iv_renten', period)
        bvg = person('einkommen_berufliche_vorsorge', period)
        saeule3a = person('einkommen_gebundene_selbstvorsorge', period)
        kapital = person('kapitalabfindung_vorsorge_rueckzahlung', period)
        leibrente = person('leibrente_steuerbarer_betrag', period)

        return ahv_iv + bvg + saeule3a + kapital + leibrente
