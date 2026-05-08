"""SR 824.0 Art. 1

Generated from: ch/824/de/824.0.md

Art. 1: Grundsatz - Persons subject to military service who cannot reconcile
military service with their conscience perform civilian service on request.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zdg_ist_militaerdienstpflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist militärdienstpflichtig"
    reference = "SR 824.0 Art. 1"


class zdg_gewissenskonflikt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Militärdienst ist mit dem Gewissen nicht vereinbar"
    reference = "SR 824.0 Art. 1"


class zdg_anspruch_zivildienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Zulassung zum Zivildienst"
    reference = "SR 824.0 Art. 1"

    def formula(person, period, parameters):
        militaerpflichtig = person('zdg_ist_militaerdienstpflichtig', period)
        gewissen = person('zdg_gewissenskonflikt', period)
        return militaerpflichtig * gewissen
