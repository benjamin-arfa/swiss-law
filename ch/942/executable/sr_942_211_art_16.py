"""SR 942.211 Art. 16

Generated from: ch/942/de/942.211.md

Art. 16: Bekanntgabe weiterer Preise - Disclosure of comparison prices:
An additional comparison price may be disclosed if:
a. Product was actually offered at the comparison price:
   1. immediately before the current price, OR
   2. for at least 30 consecutive days
b. Product will be offered at this price immediately after (introductory price)
c. Majority of competitors offer at this price (competitor comparison)

Duration limits:
- Self-comparison (a.1) and introductory price (b): max half the duration it was applied, max 2 months
- Self-comparison (a.2): unlimited duration, can be used for successive price reductions
- Perishable goods: if offered for half a day, may show as comparison for the next day
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pbv_vergleichspreis_typ(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ des Vergleichspreises (1=Selbstvergleich unmittelbar vorher, 2=Selbstvergleich 30+ Tage, 3=Einführungspreis, 4=Konkurrenzvergleich, 0=keiner)"
    reference = "SR 942.211 Art. 16 Abs. 1"


class pbv_vergleichspreis_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vergleichspreis (CHF)"
    reference = "SR 942.211 Art. 16 Abs. 1"


class pbv_dauer_vergleichspreis_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer, die der Vergleichspreis gehandhabt wurde (Tage)"
    reference = "SR 942.211 Art. 16 Abs. 3"


class pbv_mindestdauer_30_tage_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vergleichspreis wurde mindestens 30 aufeinanderfolgende Tage angeboten"
    reference = "SR 942.211 Art. 16 Abs. 1 Bst. a Ziff. 2"

    def formula(person, period, parameters):
        dauer = person('pbv_dauer_vergleichspreis_tage', period)
        return dauer >= 30


class pbv_vergleichspreis_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vergleichspreis darf bekanntgegeben werden"
    reference = "SR 942.211 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        typ = person('pbv_vergleichspreis_typ', period)
        dauer = person('pbv_dauer_vergleichspreis_tage', period)

        # Type 1: immediate self-comparison (was offered immediately before)
        typ1_ok = typ == 1
        # Type 2: 30+ days self-comparison
        typ2_ok = (typ == 2) * (dauer >= 30)
        # Type 3: introductory price (will be offered after)
        typ3_ok = typ == 3
        # Type 4: competitor comparison
        typ4_ok = typ == 4

        return (typ1_ok + typ2_ok + typ3_ok + typ4_ok) > 0


class pbv_vergleichspreis_max_dauer_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer der Bekanntgabe des Vergleichspreises (Tage)"
    reference = "SR 942.211 Art. 16 Abs. 3"

    def formula(person, period, parameters):
        typ = person('pbv_vergleichspreis_typ', period)
        dauer = person('pbv_dauer_vergleichspreis_tage', period)

        # Type 1 and 3: max half the original duration, capped at 60 days (2 months)
        halb = np.minimum(dauer // 2, 60)
        # Type 2: unlimited (set to 9999)
        result = np.select(
            [typ == 1, typ == 2, typ == 3, typ == 4],
            [halb, 9999, halb, 9999],
            default=0
        )
        return result
