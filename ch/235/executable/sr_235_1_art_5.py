"""SR 235.1 Art. 5

Generated from: ch/235/de/235.1.md

Richtigkeit der Daten: Pflicht zur Vergewisserung ueber Richtigkeit,
Berichtigungs-/Vernichtungspflicht, Berichtigungsrecht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_daten_richtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Personendaten sind richtig und vollstaendig"
    reference = "SR 235.1 Art. 5 Abs. 1"


class dsg_berichtigungspflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pflicht zur Berichtigung oder Vernichtung unrichtiger/unvollstaendiger Daten"
    reference = "SR 235.1 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        richtig = person('dsg_daten_richtig', period)
        return not_(richtig)


class dsg_berichtigungsrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person kann Berichtigung unrichtiger Daten verlangen"
    reference = "SR 235.1 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        richtig = person('dsg_daten_richtig', period)
        return not_(richtig)
