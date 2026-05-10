"""SR 232.14 Art. 1

Generated from: ch/232/de/232.14.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erfindung_ist_neu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ist neu (gehört nicht zum Stand der Technik)"
    reference = "SR 232.14 Art. 1 Abs. 1"


class erfindung_gewerblich_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ist gewerblich anwendbar"
    reference = "SR 232.14 Art. 1 Abs. 1"


class erfindung_erfinderische_taetigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ergibt sich nicht in naheliegender Weise aus dem Stand der Technik"
    reference = "SR 232.14 Art. 1 Abs. 2"


class erfindung_patentierbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ist patentierbar"
    reference = "SR 232.14 Art. 1"

    def formula(person, period, parameters):
        neu = person('erfindung_ist_neu', period)
        gewerblich = person('erfindung_gewerblich_anwendbar', period)
        erfinderisch = person('erfindung_erfinderische_taetigkeit', period)
        return neu * gewerblich * erfinderisch
