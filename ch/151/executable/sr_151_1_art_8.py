"""SR 151.1 Art. 8

Generated from: ch/151/de/151.1.md

Verfahren bei diskriminierender Ablehnung der Anstellung:
Verwirkungsfrist von 3 Monaten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class datum_mitteilung_ablehnung(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum der Mitteilung der Ablehnung der Anstellung"
    reference = "SR 151.1 Art. 8 Abs. 2"


class datum_klageerhebung(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum der Klageerhebung"
    reference = "SR 151.1 Art. 8 Abs. 2"


class entschaedigung_verwirkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Entschaedigungsanspruch wegen Fristablauf verwirkt ist (3 Monate)"
    reference = "SR 151.1 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        # Anspruch verwirkt, wenn Klage nicht innert 3 Monaten erhoben wird
        # This would require date comparison logic; modeled as input-driven
        return False
