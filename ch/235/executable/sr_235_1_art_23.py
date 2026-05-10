"""SR 235.1 Art. 23

Generated from: ch/235/de/235.1.md

Privatrechtliche Taetigkeit von Bundesorganen: Bei privatrechtlichem
Handeln gelten die Bestimmungen fuer private Personen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_bundesorgan_handelt_privatrechtlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesorgan handelt privatrechtlich"
    reference = "SR 235.1 Art. 23 Abs. 1"


class dsg_privatrecht_bestimmungen_gelten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bestimmungen fuer private Personen gelten fuer das Bundesorgan"
    reference = "SR 235.1 Art. 23"

    def formula(person, period, parameters):
        return person('dsg_bundesorgan_handelt_privatrechtlich', period)
