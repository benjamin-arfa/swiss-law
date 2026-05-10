"""SR 196.1 Art. 13

Generated from: ch/196/de/196.1.md

Uebermittlung von Informationen an den Herkunftsstaat: Regeln fuer die
Weitergabe von Bankinformationen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class staatliche_strukturen_versagen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die staatlichen Strukturen im Herkunftsstaat versagen"
    reference = "SR 196.1 Art. 13 Abs. 3 lit. a"


class uebermittlung_gefaehrdet_leben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob durch die Uebermittlung das Leben oder die koerperliche Unversehrtheit der Betroffenen gefaehrdet wuerde"
    reference = "SR 196.1 Art. 13 Abs. 3 lit. b"


class informationsuebermittlung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Uebermittlung von Informationen ins Ausland zulaessig ist"
    reference = "SR 196.1 Art. 13 Abs. 3"

    def formula(person, period, parameters):
        versagen = person('staatliche_strukturen_versagen', period)
        gefaehrdung = person('uebermittlung_gefaehrdet_leben', period)
        return (1 - versagen) * (1 - gefaehrdung)
