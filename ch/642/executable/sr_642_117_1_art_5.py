"""SR 642.117.1 Art. 5

Generated from: ch/642/de/642.117.1.md

Art. 5: Assessment upon reaching majority
(Veranlagung bei Eintritt der Volljaehrigkeit)

Abs. 1: Taxpayers are first separately assessed for the tax period
in which they reach majority.
Abs. 2: Minors are separately assessed if they earn employment income
(Art. 9 Abs. 2 DBG) or are not under parental authority.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ifd_volljaehrig_in_steuerperiode(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person wird in dieser Steuerperiode volljaehrig"
    reference = "SR 642.117.1 Art. 5 Abs. 1"


class ifd_minderjaehrig_erwerbseinkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Minderjaehrige Person mit eigenem Erwerbseinkommen (Art. 9 Abs. 2 DBG)"
    reference = "SR 642.117.1 Art. 5 Abs. 2"


class ifd_nicht_unter_elterlicher_sorge(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person steht nicht unter elterlicher Sorge"
    reference = "SR 642.117.1 Art. 5 Abs. 2"


class ifd_separat_veranlagt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person wird separat veranlagt"
    reference = "SR 642.117.1 Art. 5"

    def formula(person, period, parameters):
        volljaehrig = person('ifd_volljaehrig_in_steuerperiode', period)
        erwerbs_mj = person('ifd_minderjaehrig_erwerbseinkommen', period)
        keine_sorge = person('ifd_nicht_unter_elterlicher_sorge', period)
        return volljaehrig + erwerbs_mj + keine_sorge
