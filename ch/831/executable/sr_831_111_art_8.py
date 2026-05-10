"""SR 831.111 Art. 8

Generated from: ch/831/de/831.111.md

Art. 8: Fristen und Modalitaeten - Deadlines and modalities for joining.

Abs. 1: Declaration of accession must be submitted in writing to the
compensation office within one year of leaving mandatory insurance.
After expiry, joining is no longer possible.

Abs. 2: Insurance begins when leaving mandatory insurance.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vfv_datum_ausscheiden_obligatorisch(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = MONTH
    label = "Datum des Ausscheidens aus der obligatorischen Versicherung"
    reference = "SR 831.111 Art. 8 Abs. 1"


class vfv_beitrittserklaerung_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitrittserklaerung wurde schriftlich bei der Ausgleichskasse eingereicht"
    reference = "SR 831.111 Art. 8 Abs. 1"


class vfv_beitrittsfrist_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitrittsfrist von einem Jahr seit Ausscheiden eingehalten (Art. 8 Abs. 1 VFV)"
    reference = "SR 831.111 Art. 8 Abs. 1"
