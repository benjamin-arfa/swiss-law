"""SR 128.51 Art. 16

Generated from: ch/128/de/128.51.md

Frist zur Erfassung der Meldung: If not all information is available within
the 24-hour reporting deadline, BACS grants 14 additional days to complete.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alle_infos_innerhalb_24h_bekannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle erforderlichen Informationen innerhalb der 24-Stunden-Meldefrist bekannt sind"
    reference = "SR 128.51 Art. 16 Abs. 1"


class ergaenzungsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist in Tagen zur Ergaenzung der Meldung"
    reference = "SR 128.51 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        infos_bekannt = person('alle_infos_innerhalb_24h_bekannt', period)
        return np.where(infos_bekannt, 0, 14)
