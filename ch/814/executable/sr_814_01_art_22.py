"""SR 814.01 Art. 22

Generated from: ch/fr/814/814.01.md

Art. 22: Permis de construire dans les zones affectees par le bruit
  (Baubewilligung in laermbelasteten Gebieten)
- Abs. 1: Building permit for dwellings only if immission limit values can be met.
- Abs. 2: If limits cannot be met, permit only with specific noise protection measures:
  controlled ventilation, cooling, or at least half rooms with compliant windows.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class usg_baugesuch_fuer_wohnnutzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Baugesuch fuer Wohnnutzung vorliegt"
    reference = "SR 814.01 Art. 22 Abs. 1"


class usg_igw_laerm_am_standort_einhaltbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Laerm-Immissionsgrenzwerte am Baustandort eingehalten werden koennen"
    reference = "SR 814.01 Art. 22 Abs. 1"


class usg_kontrollierte_lueftung_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob kontrollierte Wohnungslueftung vorgesehen ist"
    reference = "SR 814.01 Art. 22 Abs. 2 Bst. a Ziff. 1"


class usg_haelfte_raeume_igw_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob mindestens die Haelfte der laermempfindlichen Raeume IGW-konforme Fenster hat"
    reference = "SR 814.01 Art. 22 Abs. 2 Bst. a Ziff. 2"


class usg_baubewilligung_laermgebiet_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Baubewilligung im laermbelasteten Gebiet erteilt werden kann"
    reference = "SR 814.01 Art. 22"

    def formula(person, period, parameters):
        wohnnutzung = person('usg_baugesuch_fuer_wohnnutzung', period)
        igw_ok = person('usg_igw_laerm_am_standort_einhaltbar', period)
        lueftung = person('usg_kontrollierte_lueftung_vorhanden', period)
        haelfte = person('usg_haelfte_raeume_igw_konform', period)

        # Not for residential: always ok
        # Residential + IGW met: ok
        # Residential + IGW not met: need ventilation or half rooms compliant
        return not_(wohnnutzung) + (wohnnutzung * igw_ok) + (
            wohnnutzung * not_(igw_ok) * (lueftung + haelfte))
