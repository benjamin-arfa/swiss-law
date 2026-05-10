"""SR 922.0 Art. 4

Generated from: ch/922/de/922.0.md

Art. 4: Jagdberechtigung - Hunting authorization:
1. Anyone who wants to hunt needs a cantonal hunting authorization
2. Authorization is granted to applicants who pass a cantonal examination
3. Cantons may grant limited (day-based) authorization to exam preparers and hunting guests
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jsg_jagdpruefung_bestanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat die kantonale Jagdprüfung bestanden"
    reference = "SR 922.0 Art. 4 Abs. 2"


class jsg_ist_jagdgast(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Jagdgast"
    reference = "SR 922.0 Art. 4 Abs. 3"


class jsg_bereitet_jagdpruefung_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bereitet sich auf die Jagdprüfung vor"
    reference = "SR 922.0 Art. 4 Abs. 3"


class jsg_jagdberechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat eine kantonale Jagdberechtigung"
    reference = "SR 922.0 Art. 4"

    def formula(person, period, parameters):
        pruefung = person('jsg_jagdpruefung_bestanden', period)
        jagdgast = person('jsg_ist_jagdgast', period)
        vorbereitung = person('jsg_bereitet_jagdpruefung_vor', period)
        # Full authorization via exam, or limited via guest/preparation status
        return pruefung + jagdgast + vorbereitung > 0
