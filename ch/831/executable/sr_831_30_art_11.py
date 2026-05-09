"""SR 831.30 Art. 11

Generated from: ch/831/de/831.30.md

Art. 11: Anrechenbare Einnahmen - Countable income for EL calculation.

Abs. 1:
a. 2/3 of employment income exceeding CHF 1,300/yr (single) or
   CHF 1,950/yr (couples/with children); for spouses without EL
   entitlement: 80%; for IV daily allowance recipients: 100%
b. Income from movable and immovable assets, including usufruct/rental value
c. 1/15 of net assets (1/10 for old-age pensioners) exceeding:
   - CHF 30,000 (single)
   - CHF 50,000 (couples)
   - CHF 15,000 (orphans/children)
   Owner-occupied property: only value exceeding CHF 112,500 counts
d. Pensions, including AHV/IV pensions
e. Verpfruendung benefits
f. Family allowances
h. Maintenance payments received
i. Premium reductions for retroactive EL periods

Abs. 1bis: For owner-occupied property with spouse in home/hospital or
helplessness allowance recipient: only value exceeding CHF 300,000 counts.

Abs. 3: Not counted: family support (Art. 328-330 ZGB), social welfare,
charitable benefits, helplessness allowances, scholarships, AHV/IV
assistance contributions, nursing insurance in homes, pension supplement
(Art. 34bis AHVG), 13th old-age pension (Art. 34ter AHVG).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_erwerbseinkommen_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Erwerbseinkommen"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"


class el_bezieht_iv_taggeld(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bezieht IV-Taggeld"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"


class el_ehegatte_ohne_el_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ehegatte ohne eigenen EL-Anspruch"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"


class el_erwerbseinkommen_anrechenbar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbares Erwerbseinkommen (Art. 11 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        brutto = person('el_erwerbseinkommen_brutto', period)
        alleinstehend = person('el_ist_alleinstehend', period.first_month)
        iv_taggeld = person('el_bezieht_iv_taggeld', period.first_month)
        ehegatte_ohne_el = person('el_ehegatte_ohne_el_anspruch', period.first_month)

        # Freibetrag: CHF 1,300 (single) or CHF 1,950 (couple/with children)
        freibetrag = where(alleinstehend, 1300, 1950)

        # IV daily allowance recipients: 100% counted
        # Spouses without EL: 80% counted
        # Others: 2/3 counted
        anrechenbar = where(
            iv_taggeld,
            brutto,
            where(
                ehegatte_ohne_el,
                max_(brutto - freibetrag, 0) * 0.80,
                max_(brutto - freibetrag, 0) * (2.0 / 3.0),
            ),
        )
        return anrechenbar


class el_vermoegensertraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus beweglichem und unbeweglichem Vermoegen (Art. 11 Abs. 1 Bst. b ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. b"


class el_ist_altersrentner(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Altersrentnerin oder Altersrentner"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. c"


class el_bewohnte_liegenschaft_wert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wert der selbst bewohnten Liegenschaft"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. c"


class el_vermoegensverzehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbarer Vermoegensverzehr (Art. 11 Abs. 1 Bst. c ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        vermoegen = person('el_reinvermoegen', period)
        alleinstehend = person('el_ist_alleinstehend', period.first_month)
        ehepaar = person('el_ist_ehepaar', period.first_month)
        waise = person('el_ist_waise_oder_kind', period.first_month)
        ist_altersrentner = person('el_ist_altersrentner', period.first_month)

        # Freibetraege
        freibetrag = select(
            [waise, ehepaar, alleinstehend],
            [15000, 50000, 30000],
            default=30000,
        )

        # Owner-occupied property: only value above CHF 112,500 counts
        liegenschaft = person('el_bewohnte_liegenschaft_wert', period)
        liegenschaft_anrechenbar = max_(liegenschaft - 112500, 0)

        # Total assessable assets
        vermoegen_anrechenbar = max_(
            vermoegen - liegenschaft + liegenschaft_anrechenbar - freibetrag,
            0,
        )

        # 1/10 for old-age pensioners, 1/15 for others
        rate = where(ist_altersrentner, 1.0 / 10.0, 1.0 / 15.0)

        return vermoegen_anrechenbar * rate


class el_renten_pensionen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Renten, Pensionen und andere wiederkehrende Leistungen (Art. 11 Abs. 1 Bst. d ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. d"


class el_familienzulagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Familienzulagen (Art. 11 Abs. 1 Bst. f ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. f"


class el_unterhaltsbeitraege_erhalten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erhaltene familienrechtliche Unterhaltsbeitraege (Art. 11 Abs. 1 Bst. h ELG)"
    reference = "SR 831.30 Art. 11 Abs. 1 Bst. h"


class el_einnahmen_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total anrechenbare Einnahmen (Art. 11 ELG)"
    reference = "SR 831.30 Art. 11"

    def formula(person, period, parameters):
        erwerb = person('el_erwerbseinkommen_anrechenbar', period)
        vermoegensertrag = person('el_vermoegensertraege', period)
        verzehr = person('el_vermoegensverzehr', period)
        renten = person('el_renten_pensionen', period)
        familienzulagen = person('el_familienzulagen', period)
        unterhalt = person('el_unterhaltsbeitraege_erhalten', period)

        return erwerb + vermoegensertrag + verzehr + renten + familienzulagen + unterhalt
