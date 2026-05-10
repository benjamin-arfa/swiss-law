"""SR 120.4 Art. 18

Generated from: ch/120/de/120.4.md

Wiederholung: Repetition intervals for security checks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_letzter_psp(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit der letzten Personensicherheitspruefung"
    reference = "SR 120.4 Art. 18"


class psp_wiederholung_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wiederholung der PSP faellig ist"
    reference = "SR 120.4 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_letzter_psp', period)
        grundsicherheit = person('grundsicherheitspruefung_erforderlich', period)
        erweitert = person('erweiterte_psp_erforderlich', period)
        erweitert_befragung = person('erweiterte_psp_mit_befragung_erforderlich', period)

        # lit. a: 8 Jahre bei Grundsicherheitspruefung (Art. 10 Abs. 2 lit. a-e)
        faellig_grund = grundsicherheit * (jahre >= 8)

        # lit. b: 6 Jahre bei erweiterter PSP (Art. 11 Abs. 2 lit. a-f)
        faellig_erweitert = erweitert * (jahre >= 6)

        # lit. c: 5 Jahre bei erweiterter PSP mit Befragung (Art. 12)
        faellig_erweitert_befragung = erweitert_befragung * (jahre >= 5)

        return (faellig_grund + faellig_erweitert + faellig_erweitert_befragung) > 0
