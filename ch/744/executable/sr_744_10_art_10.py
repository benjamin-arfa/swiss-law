"""SR 744.10 Art. 10

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class beschwerdeverfahren_nach_bundesverwaltungsrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Beschwerdeverfahren richtet sich nach den Vorschriften der Bundesverwaltungsrechtspflege (SR 744.10 Art. 10)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1960/1025_1081_1085/de#art_10"

    def formula(person, period, parameters):
        # Art. 10 is purely procedural: appeals in matters governed by SR 744.10
        # are always subject to federal administrative law (Bundesverwaltungsrechtspflege).
        return True
