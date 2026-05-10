"""SR 441.1 Art. 5

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_amtssprache_deutsch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Deutsch ist Amtssprache des Bundes"
    reference = "SR 441.1, Art. 5 Abs. 1"

    def formula(self, period, parameters):
        return True


class ist_amtssprache_franzoesisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Französisch ist Amtssprache des Bundes"
    reference = "SR 441.1, Art. 5 Abs. 1"

    def formula(self, period, parameters):
        return True


class ist_amtssprache_italienisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Italienisch ist Amtssprache des Bundes"
    reference = "SR 441.1, Art. 5 Abs. 1"

    def formula(self, period, parameters):
        return True


class raetoromanisch_amtssprache_im_verkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rätoromanisch ist Amtssprache im Verkehr mit Personen dieser Sprache"
    reference = "SR 441.1, Art. 5 Abs. 1"

    def formula(self, period, parameters):
        ist_raetoromanischsprachig = self.person('ist_raetoromanischsprachig', period)
        return ist_raetoromanischsprachig


class ist_raetoromanischsprachig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist rätoromanischer Sprache"
    reference = "SR 441.1, Art. 5 Abs. 1"
