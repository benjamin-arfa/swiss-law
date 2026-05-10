"""SR 431.02 Art. 11

Generated from: ch/431/de/431.02.md

Meldepflicht - Anmeldung innerhalb von 14 Tagen nach Umzug.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tage_seit_umzug(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Tage seit dem Umzug"
    reference = "SR 431.02 Art. 11 Bst. a"


class anmeldung_erfolgt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anmeldung bei der zustaendigen Amtsstelle ist erfolgt"
    reference = "SR 431.02 Art. 11 Bst. a"


class meldefrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Meldefrist in Tagen nach Umzug"
    reference = "SR 431.02 Art. 11 Bst. a"
    default_value = 14


class meldepflicht_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Meldepflicht nach Umzug ist erfuellt (innerhalb 14 Tagen gemeldet)"
    reference = "SR 431.02 Art. 11 Bst. a"

    def formula(person, period, parameters):
        return (
            person('anmeldung_erfolgt', period) *
            (person('tage_seit_umzug', period) <= person('meldefrist_tage', period))
        )
