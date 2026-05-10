"""SR 363.1 Art. 16

Generated from: ch/363/de/363.1.md

Loeschung von auslaendischen Profilen bei internationaler Zusammenarbeit.
Ohne Meldung: Loeschung 30 Jahre nach Erfassung im IPAS.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auslaendisches_profil(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "DNA-Profil stammt aus internationaler Zusammenarbeit"
    reference = "SR 363.1 Art. 16"


class auslaendisches_profil_loeschverlangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auslaendische Behoerde hat Loeschung des Profils verlangt"
    reference = "SR 363.1 Art. 16"


class jahre_seit_erfassung_ipas(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit Erfassung des auslaendischen Profils im IPAS"
    reference = "SR 363.1 Art. 16"


class auslaendisches_profil_zu_loeschen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auslaendisches DNA-Profil ist zu loeschen"
    reference = "SR 363.1 Art. 16"

    def formula(person, period, parameters):
        auslaendisch = person('auslaendisches_profil', period)
        verlangen = person('auslaendisches_profil_loeschverlangen', period)
        jahre = person('jahre_seit_erfassung_ipas', period)
        return auslaendisch * (verlangen + (jahre >= 30))
