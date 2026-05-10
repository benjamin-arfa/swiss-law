"""SR 138.1 Art. 4 - Anhoerung der Kantone

Generated from: ch/138/de/138.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class kantone_verlangen_anhoerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantone verlangen eine Anhoerung"
    reference = "SR 138.1 Art. 4 Abs. 1"


class kantonale_zustaendigkeiten_betroffen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Zustaendigkeiten der Kantone sind betroffen"
    reference = "SR 138.1 Art. 4 Abs. 3"


class bund_nimmt_verhandlungen_auf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund nimmt Verhandlungen auf"
    reference = "SR 138.1 Art. 4 Abs. 2"


# Computed variables

class bund_muss_kantone_anhoeren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund muss die Kantone anhoeren"
    reference = "SR 138.1 Art. 4 Abs. 1-2"

    def formula(self, period, parameters):
        verlangen = self('kantone_verlangen_anhoerung', period)
        verhandlungen = self('bund_nimmt_verhandlungen_auf', period)
        return verlangen + verhandlungen > 0


class stellungnahme_kantone_besonderes_gewicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Den Stellungnahmen der Kantone kommt besonderes Gewicht zu"
    reference = "SR 138.1 Art. 4 Abs. 3"

    def formula(self, period, parameters):
        return self('kantonale_zustaendigkeiten_betroffen', period)
