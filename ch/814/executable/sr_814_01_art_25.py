"""SR 814.01 Art. 25

Generated from: ch/fr/814/814.01.md

Art. 25: Construction d'installations fixes (Errichtung ortsfester Anlagen)
- Abs. 1: New fixed installations may only be built if noise from the installation alone
  does not exceed planning values in the vicinity.
- Abs. 2: Relaxations possible for installations of overriding public interest,
  but immission limit values must still not be exceeded.
- Abs. 3: If source measures insufficient for new roads/airports/railways,
  nearby buildings must be protected with sound-insulation at installation owner's cost.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class usg_neue_ortsfeste_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine neue ortsfeste Anlage errichtet werden soll"
    reference = "SR 814.01 Art. 25 Abs. 1"


class usg_planungswerte_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Planungswerte fuer Laerm eingehalten werden"
    reference = "SR 814.01 Art. 25 Abs. 1"


class usg_oeffentliches_interesse_ueberwiegend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob ein ueberwiegendes oeffentliches Interesse an der Anlage besteht"
    reference = "SR 814.01 Art. 25 Abs. 2"


class usg_neue_anlage_bewilligungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die neue ortsfeste Anlage bewilligungsfaehig ist bezueglich Laerm"
    reference = "SR 814.01 Art. 25"

    def formula(person, period, parameters):
        neue_anlage = person('usg_neue_ortsfeste_anlage', period)
        planungswerte = person('usg_planungswerte_eingehalten', period)
        oeff_interesse = person('usg_oeffentliches_interesse_ueberwiegend', period)
        igw = person('usg_immissionsgrenzwert_laerm_eingehalten', period)

        # Not a new installation: not relevant
        # Planning values met: ok
        # Planning values not met but public interest + IGW met: ok (relaxation)
        return not_(neue_anlage) + (neue_anlage * planungswerte) + (
            neue_anlage * not_(planungswerte) * oeff_interesse * igw)
