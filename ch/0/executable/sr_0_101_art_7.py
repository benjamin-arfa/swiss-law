"""SR 0.101 Art. 7

Generated from: ch/0/de/0.101.md

No punishment without law (nulla poena sine lege): No one shall be
held guilty of any criminal offence which did not constitute a criminal
offence at the time when it was committed. No heavier penalty than
the one applicable at the time.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_keine_strafe_ohne_gesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Grundsatz 'keine Strafe ohne Gesetz' (nulla poena sine lege) gilt"
    reference = "SR 0.101 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_keine_schwerere_strafe_rueckwirkend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verbot einer schwereren als der zur Tatzeit angedrohten Strafe gilt"
    reference = "SR 0.101 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
