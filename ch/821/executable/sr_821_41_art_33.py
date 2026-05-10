"""SR 821.41 Art. 33

Generated from: ch/821/de/821.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class freiwillige_einigungsstelle_errichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Fabrikinhaber und Arbeiter derselben Industrie haben eine "
        "freiwillige Einigungsstelle errichtet"
    )
    reference = "SR 821.41 Art. 33"


class freiwillige_einigungsstelle_ersetzt_amtliche(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Freiwillige Einigungsstelle tritt anstatt der amtlichen "
        "Einigungsstelle in Taetigkeit"
    )
    reference = "SR 821.41 Art. 33"

    def formula(person, period, parameters):
        return person('freiwillige_einigungsstelle_errichtet', period)
