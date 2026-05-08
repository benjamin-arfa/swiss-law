"""AG 290.100 § 2

Generated from: ch/ag/de/290.100.md

§ 2 Anwaltsmonopol: Procedural representation in the monopoly area is
reserved for lawyers registered in the cantonal register or enjoying
freedom of movement under BGFA.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_anwalt_im_kantonalen_register(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Im kantonalen Anwaltsregister eingetragen (AG 290.100 § 2 Abs. 2)"
    reference = "AG 290.100 § 2 Abs. 2"


class ag_freizuegigkeit_bgfa(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Geniesst Freizuegigkeit gemaess BGFA (AG 290.100 § 2 Abs. 2)"
    reference = "AG 290.100 § 2 Abs. 2"


class ag_zur_parteivertretung_zugelassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zur Parteivertretung im Monopolbereich zugelassen (AG 290.100 § 2)"
    reference = "AG 290.100 § 2 Abs. 2"

    def formula(person, period, parameters):
        im_register = person('ag_anwalt_im_kantonalen_register', period)
        freizuegigkeit = person('ag_freizuegigkeit_bgfa', period)
        return im_register + freizuegigkeit > 0
