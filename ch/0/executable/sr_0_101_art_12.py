"""SR 0.101 Art. 12

Generated from: ch/0/de/0.101.md

Right to marry: Men and women of marriageable age have the right to
marry and to found a family, according to the national laws governing
the exercise of this right.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_heiratsfaehiges_alter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person im heiratsfaehigen Alter ist"
    reference = "SR 0.101 Art. 12"


class emrk_recht_auf_eheschliessung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Eheschliessung und Familiengruendung gilt"
    reference = "SR 0.101 Art. 12"

    def formula(person, period, parameters):
        heiratsfaehig = person('emrk_heiratsfaehiges_alter', period)
        unterstellt = person('emrk_hoheitsgewalt_unterstellt', period)
        return heiratsfaehig * unterstellt
