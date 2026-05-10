"""SR 443.1 Art. 19a

Generated from: ch/443/de/443.1.md

Zugang zum Filmerbe: Vom Bund unterstuetzte Filme sind in der Cinematheque
Suisse hinterlegt. Nach 5 Jahren koennen sie oeffentlich zugaenglich gemacht werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_veroeffentlichung_film(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit Veroeffentlichung des Films"
    reference = "SR 443.1 Art. 19a Abs. 2"


class film_oeffentlich_zugaenglich_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der vom Bund unterstuetzte Film oeffentlich zugaenglich gemacht werden kann"
    reference = "SR 443.1 Art. 19a Abs. 2"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_veroeffentlichung_film', period)
        return jahre >= 5
