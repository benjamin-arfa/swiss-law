"""SR 363.1 Art. 6a

Generated from: ch/363/de/363.1.md

Verwendung der nicht in das Informationssystem aufgenommenen Spurenprofile:
lokaler Vergleich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class spur_nicht_im_informationssystem(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Spurenprofil wurde nicht in das DNA-Profil-Informationssystem aufgenommen"
    reference = "SR 363.1 Art. 6a Abs. 1"


class lokaler_vergleich_zweck(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Zweck des lokalen Vergleichs (identifikation, massenuntersuchung, isolierung, eliminierung)"
    reference = "SR 363.1 Art. 6a Abs. 2"


class personenprofil_aktiver_status(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "DNA-Profil der Person hat im Informationssystem einen aktiven Status"
    reference = "SR 363.1 Art. 6a Abs. 3"


class lokaler_vergleich_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Lokaler Vergleich mit nicht im Informationssystem aufgenommenem Spurenprofil ist zulaessig"
    reference = "SR 363.1 Art. 6a"

    def formula(person, period, parameters):
        nicht_im_system = person('spur_nicht_im_informationssystem', period)
        aktiver_status = person('personenprofil_aktiver_status', period)
        return nicht_im_system * aktiver_status
