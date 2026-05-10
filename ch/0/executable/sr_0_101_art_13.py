"""SR 0.101 Art. 13

Generated from: ch/0/de/0.101.md

Right to an effective remedy: Everyone whose Convention rights have been
violated shall have an effective remedy before a national authority.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_konventionsrecht_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verletzung der in der EMRK anerkannten Rechte oder Freiheiten vorliegt"
    reference = "SR 0.101 Art. 13"


class emrk_recht_auf_wirksame_beschwerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf eine wirksame Beschwerde bei einer innerstaatlichen Instanz besteht"
    reference = "SR 0.101 Art. 13"

    def formula(person, period, parameters):
        verletzt = person('emrk_konventionsrecht_verletzt', period)
        unterstellt = person('emrk_hoheitsgewalt_unterstellt', period)
        return verletzt * unterstellt
