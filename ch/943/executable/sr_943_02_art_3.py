"""SR 943.02 Art. 3

Generated from: ch/943/de/943.02.md

Beschränkung des freien Zugangs zum Markt:
- Ortsfremden darf der Marktzugang nicht verweigert werden
- Beschränkungen nur als Auflagen/Bedingungen und nur wenn:
  a) gleichermassen für Ortsansässige gelten
  b) zur Wahrung überwiegender öffentlicher Interessen unerlässlich
  c) verhältnismässig
- Nicht verhältnismässig wenn Herkunftsort bereits ausreichend schützt
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_ortsfremd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ortsfremd (nicht ortsansässig) ist"
    reference = "SR 943.02 Art. 3 Abs. 1"


class beschraenkung_gilt_fuer_ortsansaessige(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beschränkung gleichermassen für Ortsansässige gilt"
    reference = "SR 943.02 Art. 3 Abs. 1 Bst. a"


class beschraenkung_oeffentliches_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beschränkung zur Wahrung überwiegender öffentlicher Interessen unerlässlich ist"
    reference = "SR 943.02 Art. 3 Abs. 1 Bst. b"


class beschraenkung_verhaeltnismaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beschränkung verhältnismässig ist"
    reference = "SR 943.02 Art. 3 Abs. 1 Bst. c"


class herkunftsort_schuetzt_ausreichend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der hinreichende Schutz durch Vorschriften des Herkunftsortes erreicht wird"
    reference = "SR 943.02 Art. 3 Abs. 2 Bst. a"


class marktzugangsbeschraenkung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Marktzugangsbeschränkung zulässig ist"
    reference = "SR 943.02 Art. 3"

    def formula(person, period, parameters):
        import numpy as np
        gleich = person('beschraenkung_gilt_fuer_ortsansaessige', period)
        oeffentlich = person('beschraenkung_oeffentliches_interesse', period)
        verhaeltnism = person('beschraenkung_verhaeltnismaessig', period)
        herkunft = person('herkunftsort_schuetzt_ausreichend', period)

        # If origin already protects sufficiently, not proportionate
        effektiv_verhaeltnism = verhaeltnism * (1 - herkunft)

        return gleich * oeffentlich * effektiv_verhaeltnism
