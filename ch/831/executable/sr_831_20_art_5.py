"""SR 831.20 Art. 5

Generated from: ch/831/de/831.20.md

Art. 5: Sonderfaelle - Special cases for disability determination:
- Abs. 1: For insured persons over 20 who were not gainfully employed before
  their health impairment, disability is determined by Art. 8 Abs. 3 ATSG.
- Abs. 2: For non-employed persons under 20, disability is determined by
  Art. 8 Abs. 2 ATSG.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_alter_bei_gesundheitsbeeintraechtigung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter bei Eintritt der Gesundheitsbeeintraechtigung"
    reference = "SR 831.20 Art. 5"


class iv_erwerbstaetig_vor_beeintraechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "War vor der Gesundheitsbeeintraechtigung erwerbstaetig"
    reference = "SR 831.20 Art. 5 Abs. 1"


class iv_sonderfall_betaetigungsvergleich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Invaliditaet wird nach Betaetigungsvergleich bestimmt "
        "(ueber 20, nicht erwerbstaetig vor Beeintraechtigung, Art. 5 Abs. 1 IVG)"
    )
    reference = "SR 831.20 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        alter = person('iv_alter_bei_gesundheitsbeeintraechtigung', period)
        erwerbstaetig = person('iv_erwerbstaetig_vor_beeintraechtigung', period)
        return (alter >= 20) * (erwerbstaetig == 0)


class iv_sonderfall_minderjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Invaliditaet wird nach Art. 8 Abs. 2 ATSG bestimmt "
        "(unter 20, nicht erwerbstaetig, Art. 5 Abs. 2 IVG)"
    )
    reference = "SR 831.20 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        alter = person('iv_alter_bei_gesundheitsbeeintraechtigung', period)
        erwerbstaetig = person('iv_erwerbstaetig_vor_beeintraechtigung', period)
        return (alter < 20) * (erwerbstaetig == 0)
