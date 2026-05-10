"""SR 0.837.411 Art. 15 - Residence abroad

Art. 15:
- Par. 1: Benefits may be denied for any period of residence abroad.
- Par. 2: Special regime may be established for frontier workers.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class reside_a_etranger(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person resides abroad (Art. 15 par. 1)"
    default_value = False


class est_travailleur_frontalier(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a frontier worker (Art. 15 par. 2)"
    default_value = False


class exclusion_residence_etranger(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person excluded from benefits due to foreign residence (Art. 15)"

    def formula(person, period, parameters):
        a_etranger = person("reside_a_etranger", period)
        frontalier = person("est_travailleur_frontalier", period)
        # Frontier workers may benefit from a special regime
        return a_etranger * not_(frontalier)
