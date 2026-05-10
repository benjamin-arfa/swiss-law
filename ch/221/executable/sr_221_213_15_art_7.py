"""SR 221.213.15 Art. 7

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class geltungsbereich_mehrere_kantone(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geltungsbereich erstreckt sich auf das Gebiet mehrerer Kantone"
    reference = "SR 221.213.15 Art. 7"


class zustaendigkeit_bundesrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist zuständig für Allgemeinverbindlicherklärung"
    reference = "SR 221.213.15 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('geltungsbereich_mehrere_kantone', period)


class zustaendigkeit_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton ist zuständig für Allgemeinverbindlicherklärung"
    reference = "SR 221.213.15 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return not_(person('geltungsbereich_mehrere_kantone', period))
