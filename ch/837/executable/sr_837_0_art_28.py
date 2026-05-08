"""SR 837.0 Art. 28

Generated from: ch/837/de/837.0.md

Art. 28: Taggeld bei voruebergehend fehlender oder verminderter
Arbeitsfaehigkeit (Daily allowance during temporary incapacity)

- Abs. 1: Insured persons temporarily unable to work (illness, accident,
  pregnancy) are entitled to the full daily allowance for max 30 days per
  episode, limited to 44 daily allowances within the framework period.
- Abs. 2: Daily allowances from health or accident insurance that replace
  income are deducted from unemployment benefits.
- Abs. 4: After exhausting Abs. 1 entitlement, if still partially incapable
  and receiving daily insurance benefits:
  a. full daily allowance if at least 75% capable of working
  b. 50% reduced daily allowance if at least 50% capable
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_voruebergehend_arbeitsunfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Voruebergehend arbeitsunfaehig wegen Krankheit/Unfall/Schwangerschaft"
    reference = "SR 837.0 Art. 28 Abs. 1"


class alv_arbeitsfaehigkeit_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Arbeitsfaehigkeit in Prozent (0-100)"
    reference = "SR 837.0 Art. 28 Abs. 4"


class alv_krankheit_taggelder_bezogen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl bereits bezogene Krankheitstaggelder in der Rahmenfrist"
    reference = "SR 837.0 Art. 28 Abs. 1"


class alv_taggeld_anderer_versicherungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taggelder aus Kranken- oder Unfallversicherung (Erwerbsersatz, CHF)"
    reference = "SR 837.0 Art. 28 Abs. 2"


class alv_anspruch_krankheitstaggeld(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Taggeld bei voruebergehender Arbeitsunfaehigkeit"
    reference = "SR 837.0 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        arbeitsunfaehig = person('alv_voruebergehend_arbeitsunfaehig', period)
        bezogen = person('alv_krankheit_taggelder_bezogen', period.this_year)
        p = parameters(period).alv
        return arbeitsunfaehig * (bezogen < p.taggeld_krankheit_max_tage)


class alv_taggeld_krankheit_kuerzung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kuerzungsfaktor fuer Taggeld bei verminderter Arbeitsfaehigkeit nach Art. 28 Abs. 4"
    reference = "SR 837.0 Art. 28 Abs. 4"

    def formula(person, period, parameters):
        faehigkeit = person('alv_arbeitsfaehigkeit_prozent', period)

        # >= 75% capacity: full daily allowance (factor 1.0)
        # >= 50% capacity: 50% daily allowance (factor 0.5)
        # < 50%: no entitlement (factor 0.0)
        return where(faehigkeit >= 75, 1.0, where(faehigkeit >= 50, 0.5, 0.0))
