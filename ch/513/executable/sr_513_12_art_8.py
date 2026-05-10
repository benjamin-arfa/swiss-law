"""SR 513.12 Art. 8

Generated from: ch/513/de/513.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren"


class ist_dem_stab_zuteilbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person kann dem Stab zugeteilt oder zugewiesen werden (Art. 8 SR 513.12)"
    reference = "SR 513.12 Art. 8"

    def formula(person, period, parameters):
        # Dem Stab zugeteilt oder zugewiesen werden koennen Personen
        # nach Artikel 6 MG ab Vollendung des 18. Altersjahres.
        alter_person = person('alter', period)
        return alter_person >= 18
