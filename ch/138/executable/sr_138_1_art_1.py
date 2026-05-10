"""SR 138.1 Art. 1 - Grundsatz

Generated from: ch/138/de/138.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class aussenpolitischer_entscheid_betrifft_kantonale_zustaendigkeiten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der aussenpolitische Entscheid betrifft Zustaendigkeiten der Kantone"
    reference = "SR 138.1 Art. 1 Abs. 1"


class aussenpolitik_betrifft_wichtige_vollzugsaufgaben_kantone(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Aussenpolitik des Bundes betrifft wichtige Vollzugsaufgaben der Kantone"
    reference = "SR 138.1 Art. 1 Abs. 2"


# Computed variables

class wesentliche_interessen_kantone_beruehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wesentliche Interessen der Kantone sind beruehrt"
    reference = "SR 138.1 Art. 1 Abs. 2"

    def formula(self, period, parameters):
        return self('aussenpolitik_betrifft_wichtige_vollzugsaufgaben_kantone', period)


class kantone_wirken_mit_an_aussenpolitik(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantone wirken an der Vorbereitung aussenpolitischer Entscheide mit"
    reference = "SR 138.1 Art. 1 Abs. 1"

    def formula(self, period, parameters):
        zustaendigkeiten = self('aussenpolitischer_entscheid_betrifft_kantonale_zustaendigkeiten', period)
        interessen = self('wesentliche_interessen_kantone_beruehrt', period)
        return zustaendigkeiten + interessen > 0
