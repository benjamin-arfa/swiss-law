"""SR 641.811.31 Art. 2

Generated from: ch/641/de/641.811.31.md

Refund application: requirements per vehicle, including applicant details,
licence plate, period, transport date, recipient, wood type, volume in m3,
and total refund amount. Must be filed within one year after the levy period.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class rueckerstattungsgesuch_angaben_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Rueckerstattungsgesuch alle erforderlichen Angaben enthaelt (Art. 2 Abs. 1 Bst. a-i)"
    reference = "SR 641.811.31 Art. 2 Abs. 1"


class rueckerstattungsgesuch_frist_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch innerhalb eines Jahres nach Ablauf der Abgabeperiode eingereicht wurde"
    reference = "SR 641.811.31 Art. 2 Abs. 2"


class rueckerstattungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Einreichung des Rueckerstattungsgesuchs in Jahren"
    reference = "SR 641.811.31 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return 1
