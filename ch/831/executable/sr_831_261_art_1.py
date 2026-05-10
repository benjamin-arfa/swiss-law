"""SR 831.261 Art. 1

Generated from: ch/831/de/831.261.md

Complaint-authorized disability organizations: those listed in the
appendix are authorized to file complaints per Art. 9 IFEG.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class organisation_im_verzeichnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation im Anhang der Verordnung aufgefuehrt ist"
    reference = "SR 831.261 Art. 1"


class organisation_beschwerdeberechtigt_ifeg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschwerdeberechtigung nach Art. 9 IFEG"
    reference = "SR 831.261 Art. 1"

    def formula(person, period, parameters):
        return person('organisation_im_verzeichnis', period)
