"""SR 784.104 Art. 1

Generated from: ch/784/de/784.104.md

Geltungsbereich der AEFV:
- Gilt für alle Adressierungselemente ausser Domainnamen
- Begriffe und Abkürzungen im Anhang erklärt
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_adressierungselement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein Adressierungselement im Sinne der AEFV handelt"
    reference = "SR 784.104 Art. 1 Abs. 1"


class ist_domainname(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Domainnamen handelt (von AEFV ausgenommen)"
    reference = "SR 784.104 Art. 1 Abs. 1"


class unterliegt_aefv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Adressierungselement der AEFV unterliegt"
    reference = "SR 784.104 Art. 1"

    def formula(person, period, parameters):
        return (
            person('ist_adressierungselement', period) *
            (person('ist_domainname', period) == False)
        )
