"""SR 241 Art. 2

Generated from: ch/de/241.md

General clause: Any deceptive or otherwise bad-faith conduct
that affects the relationship between competitors or between
suppliers and customers is unfair and unlawful.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class verhalten_taeuschend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verhalten taeuschend ist"
    reference = "SR 241 Art. 2"


class verhalten_gegen_treu_und_glauben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verhalten gegen den Grundsatz von Treu und Glauben verstoesst"
    reference = "SR 241 Art. 2"


class beeinflusst_wettbewerbsverhaeltnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verhalten das Verhaeltnis zwischen Mitbewerbern oder Anbietern und Abnehmern beeinflusst"
    reference = "SR 241 Art. 2"


class unlauterer_wettbewerb_grundsatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob unlauterer Wettbewerb nach Art. 2 UWG vorliegt"
    reference = "SR 241 Art. 2"

    def formula(person, period, parameters):
        taeuschend = person('verhalten_taeuschend', period)
        treu_glauben = person('verhalten_gegen_treu_und_glauben', period)
        beeinflusst = person('beeinflusst_wettbewerbsverhaeltnis', period)
        return (taeuschend + treu_glauben > 0) * beeinflusst
