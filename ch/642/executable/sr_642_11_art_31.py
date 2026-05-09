"""SR 642.11 Art. 31

Generated from: ch/642/de/642.11.md

Art. 31 Verluste (Losses):
1. Losses from the seven fiscal years preceding the tax period (Art. 40)
   may be deducted, provided they could not be taken into account when
   computing taxable income for those years.
2. Third-party contributions made to offset a deficit in the context of a
   restructuring may also be offset against losses from earlier fiscal years
   that could not yet be offset against income.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ifd_verluste_vorjahr_1(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 1. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verluste_vorjahr_2(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 2. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verluste_vorjahr_3(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 3. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verluste_vorjahr_4(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 4. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verluste_vorjahr_5(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 5. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verluste_vorjahr_6(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 6. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verluste_vorjahr_7(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Noch nicht verrechneter Verlust aus dem 7. Vorjahr (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"


class ifd_verlustvortrag_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total verrechenbarer Verlustvortrag aus den letzten 7 Jahren (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"

    def formula(person, period, parameters):
        v1 = person('ifd_verluste_vorjahr_1', period)
        v2 = person('ifd_verluste_vorjahr_2', period)
        v3 = person('ifd_verluste_vorjahr_3', period)
        v4 = person('ifd_verluste_vorjahr_4', period)
        v5 = person('ifd_verluste_vorjahr_5', period)
        v6 = person('ifd_verluste_vorjahr_6', period)
        v7 = person('ifd_verluste_vorjahr_7', period)
        return v1 + v2 + v3 + v4 + v5 + v6 + v7


class ifd_steuerbares_einkommen_vor_verlust(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbares Einkommen vor Verlustverrechnung (CHF)"
    reference = "SR 642.11 Art. 31"


class ifd_einkommen_nach_verlustverrechnung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbares Einkommen nach Verlustverrechnung (CHF)"
    reference = "SR 642.11 Art. 31 Abs. 1"

    def formula(person, period, parameters):
        einkommen = person('ifd_steuerbares_einkommen_vor_verlust', period)
        verlustvortrag = person('ifd_verlustvortrag_total', period)

        # Losses reduce income but cannot create a negative taxable income
        return max_(einkommen - verlustvortrag, 0)
