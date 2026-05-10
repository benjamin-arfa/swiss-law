"""SR 152.21 Art. 7

Generated from: ch/152/de/152.21.md

Extension of protection period: the 30- or 50-year period can be extended
on a case-by-case basis if an overriding public or private interest
exists against third-party access.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ueberwiegendes_schutzwuerdiges_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein ueberwiegendes schutzwuerdiges oeffentliches oder privates Interesse gegen Einsichtnahme vorliegt"
    reference = "SR 152.21 Art. 7 Abs. 1"


class schutzfrist_verlaengert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schutzfrist im Einzelfall verlaengert wurde"
    reference = "SR 152.21 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('ueberwiegendes_schutzwuerdiges_interesse', period)
