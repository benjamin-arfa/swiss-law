"""SR 138.1 Art. 5 - Mitwirkung bei der Vorbereitung von Verhandlungsmandaten und bei Verhandlungen

Generated from: ch/138/de/138.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aussenpolitisches_vorhaben_betrifft_kantonale_zustaendigkeiten_art5(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aussenpolitische Vorhaben betreffen die Zustaendigkeiten der Kantone"
    reference = "SR 138.1 Art. 5 Abs. 1"


class bund_muss_kantonsvertreter_beiziehen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund zieht Vertreterinnen und Vertreter der Kantone fuer die Vorbereitung der Verhandlungsmandate und Verhandlungen bei"
    reference = "SR 138.1 Art. 5 Abs. 1"

    def formula(self, period, parameters):
        return self('aussenpolitisches_vorhaben_betrifft_kantonale_zustaendigkeiten_art5', period)
