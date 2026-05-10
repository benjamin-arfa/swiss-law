"""SR 427.72 Art. 1

Generated from: ch/427/de/427.72.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_grundlagenforschung_rein_wissenschaftlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Forschungsarbeit ist Grundlagenforschung mit rein wissenschaftlicher Zielsetzung"
    reference = "SR 427.72 Art. 1 Abs. 2"


class ist_industrienahe_forschung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Forschungsarbeit ist industrienahe Forschung"
    reference = "SR 427.72 Art. 1 Abs. 2"


class forschung_im_bereich_strassenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Forschungsarbeit betrifft Aufgaben im Bereich des Strassenverkehrs"
    reference = "SR 427.72 Art. 1 Abs. 1"


class anspruch_forschungsbeitrag_strassenwesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Forschungsbeitrag des ASTRA im Strassenwesen"
    reference = "SR 427.72 Art. 1"

    def formula(person, period, parameters):
        strassenverkehr = person('forschung_im_bereich_strassenverkehr', period)
        grundlagen = person('ist_grundlagenforschung_rein_wissenschaftlich', period)
        industrienah = person('ist_industrienahe_forschung', period)
        return strassenverkehr * not_(grundlagen) * not_(industrienah)
