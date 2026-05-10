"""SR 282.11 Art. 19 - Stimmrecht

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class obligation_im_eigentum_der_schuldnerin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Obligation steht im Eigentum oder in Nutzniessung der Schuldnerin"
    reference = "SR 282.11 Art. 19 Abs. 2"


class obligation_in_nutzniessung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Obligation steht in Nutzniessung eines Dritten"
    reference = "SR 282.11 Art. 19 Abs. 1"


class stimmrecht_hat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat Stimmrecht in der Glaeubigerversammlung"
    reference = "SR 282.11 Art. 19"

    def formula(self, period, parameters):
        eigentum_schuldnerin = self('obligation_im_eigentum_der_schuldnerin', period)
        # Obligationen der Schuldnerin geben kein Stimmrecht
        return 1 - eigentum_schuldnerin
