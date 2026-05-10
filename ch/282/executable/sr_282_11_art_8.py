"""SR 282.11 Art. 8 - Anstalten und oeffentliche Waldungen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class vermoegenswert_ist_anstalt_oder_werk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert ist eine Anstalt, ein Werk, oeffentlicher Wald, Weide oder Alp"
    reference = "SR 282.11 Art. 8 Abs. 1"


class zustimmung_kantonsregierung_pfaendung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantonsregierung hat der Pfaendung und Verwertung zugestimmt"
    reference = "SR 282.11 Art. 8 Abs. 1"


# Computed variables

class anstalt_pfaendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Anstalt oder das Werk darf gepfaendet und verwertet werden"
    reference = "SR 282.11 Art. 8 Abs. 1"

    def formula(self, period, parameters):
        ist_anstalt = self('vermoegenswert_ist_anstalt_oder_werk', period)
        zustimmung = self('zustimmung_kantonsregierung_pfaendung', period)
        return ist_anstalt * zustimmung
