"""SR 831.30 Art. 11

Generated from: ch/831/de/831.30.md

Art. 11: Anrechenbare Einnahmen (Countable income)

Abs. 1 Bst. a: 2/3 of earned income exceeding:
  - Single: CHF 1,300/year
  - Couples/families: CHF 1,950/year
  For spouses without EL entitlement: 80% of earnings
  For invalid persons with IV daily allowance: 100% of earnings

Abs. 1 Bst. c: Wealth consumption (Vermoegensverzehr):
  - 1/15 of net wealth exceeding thresholds (1/10 for old-age pensioners)
  - Single: above CHF 30,000
  - Couples: above CHF 50,000
  - Children: above CHF 15,000
  - Owner-occupied property: only value above CHF 112,500 counts
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_erwerbseinkommen_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttoerwerbseinkommen in CHF pro Jahr"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"


class el_ehegatte_ohne_el_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Ehegatte ohne eigenen Anspruch auf Ergaenzungsleistungen"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"


class el_bezieht_iv_taggeld(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Invalide Person mit Anspruch auf Taggeld der IV"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"


class el_ist_altersrentner(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bezieht eine Altersrente der AHV"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. c"


class el_liegenschaftswert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wert der selbstbewohnten Liegenschaft in CHF"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. c"


class el_renten_und_pensionen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Renten, Pensionen und andere wiederkehrende Leistungen pro Jahr"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. d"


class el_anrechenbares_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbares Erwerbseinkommen (Art. 11 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        import numpy as np
        brutto = person('el_erwerbseinkommen_brutto', period)
        ist_verheiratet = person('el_ist_verheiratet', period)
        ehegatte_ohne_el = person('el_ehegatte_ohne_el_anspruch', period)
        bezieht_iv_taggeld = person('el_bezieht_iv_taggeld', period)

        # Franchise amounts
        franchise_single = 1300.0
        franchise_couple = 1950.0
        franchise = np.where(ist_verheiratet, franchise_couple, franchise_single)

        # Standard case: 2/3 of income above franchise
        standard = np.maximum(brutto - franchise, 0.0) * (2.0 / 3.0)

        # Spouse without EL: 80% of earnings (no franchise)
        ehegatte_betrag = brutto * 0.80

        # IV daily allowance: 100% of earnings (no franchise)
        iv_betrag = brutto

        return np.where(
            bezieht_iv_taggeld, iv_betrag,
            np.where(ehegatte_ohne_el, ehegatte_betrag, standard)
        )


class el_anrechenbarer_vermoegensverzehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbarer Vermoegensverzehr (Art. 11 Abs. 1 Bst. c ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        import numpy as np
        reinvermoegen = person('el_reinvermoegen', period)
        ist_verheiratet = person('el_ist_verheiratet', period)
        ist_waise = person('el_ist_waise_oder_kind_mit_kinderrente', period)
        ist_altersrentner = person('el_ist_altersrentner', period)
        liegenschaft = person('el_liegenschaftswert', period)
        bewohnt_eigene = person('el_bewohnt_eigene_liegenschaft', period)

        # Wealth thresholds (Freibetraege)
        freibetrag = np.where(
            ist_waise, 15000.0,
            np.where(ist_verheiratet, 50000.0, 30000.0)
        )

        # For owner-occupied property: only value above 112,500 counts
        liegenschaft_anrechenbar = np.where(
            bewohnt_eigene,
            np.maximum(liegenschaft - 112500.0, 0.0),
            0.0
        )

        # Total countable wealth
        vermoegen_anrechenbar = np.maximum(
            reinvermoegen + liegenschaft_anrechenbar - freibetrag, 0.0
        )

        # Consumption rate: 1/15 general, 1/10 for old-age pensioners
        rate = np.where(ist_altersrentner, 1.0 / 10.0, 1.0 / 15.0)

        return vermoegen_anrechenbar * rate


class el_anrechenbare_einnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total anrechenbare Einnahmen (Art. 11 ELG)"
    reference = "SR 831.30 Art. 11"

    def formula(person, period, parameters):
        erwerbseinkommen = person('el_anrechenbares_erwerbseinkommen', period)
        vermoegensverzehr = person('el_anrechenbarer_vermoegensverzehr', period)
        renten = person('el_renten_und_pensionen', period)

        return erwerbseinkommen + vermoegensverzehr + renten
