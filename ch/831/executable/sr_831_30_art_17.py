"""SR 831.30 Art. 17

Generated from: ch/831/de/831.30.md

Art. 17: Beitraege - Federal contributions to charitable institutions.

Abs. 1: The Confederation pays annually:
a. max CHF 16.5 million to Pro Senectute
b. max CHF 14.5 million to Pro Infirmis
c. max CHF 2.7 million to Pro Juventute

Abs. 2: The Federal Council raises the contribution caps when pensions
are re-set under Art. 33ter AHVG.

Abs. 3: The Federal Council sets the annual contribution amounts and
regulates the distribution between central and cantonal/regional bodies.

Abs. 4: Contributions to Pro Senectute and Pro Juventute are funded from
AHV resources; those to Pro Infirmis from IV resources.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_beitrag_pro_senectute(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Bundesbeitrag an Pro Senectute (max. CHF 16.5 Mio, Art. 17 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 17 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        import numpy as np
        return np.full(len(person.ids), 16500000.0)


class el_beitrag_pro_infirmis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Bundesbeitrag an Pro Infirmis (max. CHF 14.5 Mio, Art. 17 Abs. 1 Bst. b ELG)"
    reference = "SR 831.30 Art. 17 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        import numpy as np
        return np.full(len(person.ids), 14500000.0)


class el_beitrag_pro_juventute(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Bundesbeitrag an Pro Juventute (max. CHF 2.7 Mio, Art. 17 Abs. 1 Bst. c ELG)"
    reference = "SR 831.30 Art. 17 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        import numpy as np
        return np.full(len(person.ids), 2700000.0)


class el_beitraege_gemeinnuetzig_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamter Bundesbeitrag an gemeinnuetzige Institutionen (Art. 17 ELG)"
    reference = "SR 831.30 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        senectute = person('el_beitrag_pro_senectute', period)
        infirmis = person('el_beitrag_pro_infirmis', period)
        juventute = person('el_beitrag_pro_juventute', period)
        return senectute + infirmis + juventute
