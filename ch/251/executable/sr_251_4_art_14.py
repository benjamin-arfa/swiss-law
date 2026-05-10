"""SR 251.4 Art. 14

Generated from: ch/251/de/251.4.md

Bestaetigung der Vollstaendigkeit: Das Sekretariat bestaetigt innert
10 Tagen den Eingang und die Vollstaendigkeit der Meldung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class meldung_eingang_datum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Eingangs der Meldung beim Sekretariat"
    reference = "SR 251.4 Art. 14"


class frist_vollstaendigkeitsbestaetigung_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Bestaetigung der Vollstaendigkeit in Tagen (10 Tage)"
    reference = "SR 251.4 Art. 14"

    def formula(person, period, parameters):
        return 10


class meldung_ist_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Meldung vollstaendig ist"
    reference = "SR 251.4 Art. 14"
