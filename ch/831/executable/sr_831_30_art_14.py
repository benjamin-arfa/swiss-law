"""SR 831.30 Art. 14

Generated from: ch/831/de/831.30.md

Art. 14: Krankheits- und Behinderungskosten - Cantons reimburse EL
recipients for documented illness and disability costs in the current year:
a. dental treatment
b. home care, day structures
bbis. temporary home/hospital stays (max 3 months)
c. medically ordered therapeutic baths/rest cures
d. diet
e. transport to nearest treatment facility
f. aids
g. cost-sharing per Art. 64 KVG

Abs. 3: Minimum annual reimbursement caps:
At home:
  1. Single/widowed, spouse of person in home: CHF 25,000
  2. Couples: CHF 50,000
  3. Orphans: CHF 10,000
In home/hospital: CHF 6,000

Abs. 4: For persons at home with severe helplessness (IV/UV): up to
CHF 90,000, insofar as not covered by helplessness/assistance allowance.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_krankheitskosten_effektiv(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Effektive Krankheits- und Behinderungskosten (Art. 14 Abs. 1 ELG)"
    reference = "SR 831.30 Art. 14 Abs. 1"


class el_hilflosigkeit_schwer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwere Hilflosigkeit mit Anspruch auf HE der IV oder UV"
    reference = "SR 831.30 Art. 14 Abs. 4"


class el_krankheitskosten_hoechstbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstbetrag fuer Krankheits-/Behinderungskosten (Art. 14 Abs. 3 ELG)"
    reference = "SR 831.30 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        im_heim = person('el_lebt_im_heim', period.first_month)
        alleinstehend = person('el_ist_alleinstehend', period.first_month)
        ehepaar = person('el_ist_ehepaar', period.first_month)
        waise = person('el_ist_waise_oder_kind', period.first_month)
        schwere_hilflosigkeit = person('el_hilflosigkeit_schwer', period.first_month)

        # In home/hospital: CHF 6,000
        # At home - single (+ severe helplessness up to 90,000):
        betrag_zuhause = select(
            [waise, ehepaar, alleinstehend],
            [10000, 50000, 25000],
            default=25000,
        )

        # Severe helplessness increases single/widowed cap to CHF 90,000
        betrag_zuhause = where(
            schwere_hilflosigkeit * alleinstehend,
            90000,
            betrag_zuhause,
        )

        return where(im_heim, 6000, betrag_zuhause)


class el_krankheitskosten_verguetung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verguetete Krankheits- und Behinderungskosten (Art. 14 ELG)"
    reference = "SR 831.30 Art. 14"

    def formula(person, period, parameters):
        effektiv = person('el_krankheitskosten_effektiv', period)
        hoechstbetrag = person('el_krankheitskosten_hoechstbetrag', period)
        return min_(effektiv, hoechstbetrag)
