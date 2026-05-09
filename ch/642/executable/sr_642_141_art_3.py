"""SR 642.141 Art. 3

Generated from: ch/642/de/642.141.md

Art. 3: Jurisdiction in special cases
(Zustaendigkeit in Sonderfaellen)

The domicile/seat canton also means:
a. The canton with the largest share of taxable values for persons
   without tax domicile/residence/seat in Switzerland but taxable in
   multiple cantons due to economic affiliation.
b. The canton where the legal person's tax seat is located at year-end,
   if it was transferred between cantons during the tax period
   (Art. 22 Abs. 1 StHG).
c. (repealed)

Definitional article; no calculable formula.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class steuerpflicht_kein_wohnsitz_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kein steuerrechtlicher Wohnsitz/Aufenthalt/Sitz in der Schweiz"
    reference = "SR 642.141 Art. 3 Bst. a"


class steuerpflicht_sitzverlegung_interkantonal(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Sitz einer juristischen Person wurde waehrend der Steuerperiode interkantonal verlegt"
    reference = "SR 642.141 Art. 3 Bst. b"
