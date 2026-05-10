"""SR 152.3 Art. 6

Generated from: ch/152/de/152.3.md

Oeffentlichkeitsprinzip: Jede Person hat das Recht, amtliche Dokumente
einzusehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_amtliches_dokument(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein amtliches Dokument handelt"
    reference = "SR 152.3 Art. 5"


class dokument_oeffentlich_publiziert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Dokument in einem Publikationsorgan oder auf einer Internetseite des Bundes veroeffentlicht ist"
    reference = "SR 152.3 Art. 6 Abs. 3"


class recht_auf_einsichtnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Recht auf Einsichtnahme in amtliche Dokumente besteht"
    reference = "SR 152.3 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_amtliches_dokument', period)
