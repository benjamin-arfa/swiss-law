"""SR 443.14 Art. 31

Generated from: ch/443/de/443.14.md

Faelligkeit der Ersatzabgabe und Verzugszins:
- Zahlungsfrist 30 Tage ab Faelligkeit
- Nachfrist 20 Tage
- Verzugszins 5%
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ersatzabgabe_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der Ersatzabgabe (CHF)"
    reference = "SR 443.14 Art. 29"


class tage_seit_faelligkeit_ersatzabgabe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Tage seit Faelligkeit der Ersatzabgabe"
    reference = "SR 443.14 Art. 31"


class verzugszins_ersatzabgabe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verzugszins auf die Ersatzabgabe (5% p.a.)"
    reference = "SR 443.14 Art. 31 Abs. 4"

    def formula(person, period, parameters):
        betrag = person('ersatzabgabe_betrag', period)
        tage = person('tage_seit_faelligkeit_ersatzabgabe', period)
        import numpy as np
        tage_verzug = np.maximum(tage - 50, 0)
        return betrag * 0.05 * tage_verzug / 365
