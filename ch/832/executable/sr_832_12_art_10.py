"""SR 832.12 Art. 10

Generated from: ch/832/de/832.12.md

Art. 10: Beteiligungen
- Abs. 1: Versicherer muss Beteiligung an anderem Unternehmen melden,
  wenn Beteiligung 10, 20, 33 oder 50% des Kapitals/Stimmrechte erreicht.
- Abs. 2: Wer sich an einem Versicherer beteiligen will, muss dies melden
  bei gleichen Schwellen.
- Abs. 3: Herabsetzung unter die Schwellen ist ebenfalls meldepflichtig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kvag_beteiligung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Beteiligungsanteil am Versicherer oder Unternehmen in Prozent"
    reference = "SR 832.12 Art. 10"


class kvag_beteiligung_meldepflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Meldepflicht bei Beteiligung an Versicherer/Unternehmen"
    reference = "SR 832.12 Art. 10 Abs. 1-3"

    def formula(person, period, parameters):
        anteil = person('kvag_beteiligung_prozent', period)
        # Art. 10: Meldepflicht bei Erreichen/Ueberschreiten von 10, 20, 33, 50%
        return (anteil >= 10)


class kvag_beteiligung_schwelle_erreicht(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoechste erreichte Beteiligungsschwelle (10, 20, 33 oder 50%)"
    reference = "SR 832.12 Art. 10 Abs. 1-2"

    def formula(person, period, parameters):
        anteil = person('kvag_beteiligung_prozent', period)
        return select(
            [anteil >= 50, anteil >= 33, anteil >= 20, anteil >= 10],
            [50, 33, 20, 10],
            default=0,
        )
