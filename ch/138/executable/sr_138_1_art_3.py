"""SR 138.1 Art. 3 - Information der Kantone

Generated from: ch/138/de/138.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aussenpolitisches_vorhaben_betrifft_kantonale_zustaendigkeiten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das aussenpolitische Vorhaben betrifft Zustaendigkeiten der Kantone oder beruehrt deren wesentliche Interessen"
    reference = "SR 138.1 Art. 3 Abs. 2"


class bund_muss_kantone_informieren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund muss die Kantone rechtzeitig und umfassend informieren"
    reference = "SR 138.1 Art. 3 Abs. 2"

    def formula(self, period, parameters):
        return self('aussenpolitisches_vorhaben_betrifft_kantonale_zustaendigkeiten', period)
