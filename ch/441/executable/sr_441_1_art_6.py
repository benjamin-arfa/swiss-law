"""SR 441.1 Art. 6

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sprachwahl_amtssprache(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Gewählte Amtssprache für Verkehr mit Bundesbehörden"
    reference = "SR 441.1, Art. 6 Abs. 1"


class antwort_in_gewaehlter_sprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesbehörden antworten in der Amtssprache, in der sie angegangen werden"
    reference = "SR 441.1, Art. 6 Abs. 2"

    def formula(self, period, parameters):
        sprachwahl = self.person('sprachwahl_amtssprache', period)
        # If a language was chosen, authorities must respond in that language
        return sprachwahl != ''


class raetoromanisch_antwort_rumantsch_grischun(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rätoromanischsprachige erhalten Antwort in Rumantsch grischun"
    reference = "SR 441.1, Art. 6 Abs. 3"

    def formula(self, period, parameters):
        ist_raetoromanischsprachig = self.person('ist_raetoromanischsprachig', period)
        return ist_raetoromanischsprachig
