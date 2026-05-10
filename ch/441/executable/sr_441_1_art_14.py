"""SR 441.1 Art. 14

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class foerderung_schulischer_austausch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bund und Kantone fördern Austausch von Schülerinnen/Schülern und Lehrkräften aller Schulstufen"
    reference = "SR 441.1, Art. 14 Abs. 1"

    def formula(self, period, parameters):
        return True


class finanzhilfe_schulischer_austausch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bund kann Kantonen und Austauschorganisationen Finanzhilfen für schulischen Austausch gewähren"
    reference = "SR 441.1, Art. 14 Abs. 2"

    def formula(self, period, parameters):
        # Eligibility: must be a canton or exchange organization
        ist_kanton_oder_austauschorganisation = self.person('ist_kanton_oder_austauschorganisation', period)
        return ist_kanton_oder_austauschorganisation


class ist_kanton_oder_austauschorganisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Kanton oder Austauschorganisation (berechtigt für Finanzhilfe schulischer Austausch)"
    reference = "SR 441.1, Art. 14 Abs. 2"
