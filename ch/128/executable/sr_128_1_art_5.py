"""SR 128.1 Art. 5

Generated from: ch/128/de/128.1.md

Informationssicherheits-Managementsystem: Administrative units must establish
an ISMS, set annual goals, review every 3 years, and coordinate with
risk/continuity/crisis management.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_isms(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verwaltungseinheit ein ISMS erstellt hat"
    reference = "SR 128.1 Art. 5 Abs. 1"


class isms_ziele_geprueft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ISMS-Ziele jaehrlich geprueft werden"
    reference = "SR 128.1 Art. 5 Abs. 2"


class jahre_seit_letzter_isms_pruefung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit der letzten unabhaengigen ISMS-Pruefung"
    reference = "SR 128.1 Art. 5 Abs. 3"


class isms_pruefung_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine unabhaengige ISMS-Pruefung faellig ist (mindestens alle 3 Jahre)"
    reference = "SR 128.1 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        return person('jahre_seit_letzter_isms_pruefung', period) >= 3
