"""SR 0.101 Art. 8

Generated from: ch/0/de/0.101.md

Right to respect for private and family life: Everyone has the right
to respect for his private and family life, his home and his
correspondence. Interference only as prescribed by law and necessary
in a democratic society.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_recht_auf_privatleben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Achtung des Privat- und Familienlebens gilt"
    reference = "SR 0.101 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_eingriff_privatleben_gesetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Eingriff in das Privatleben gesetzlich vorgesehen ist"
    reference = "SR 0.101 Art. 8 Abs. 2"


class emrk_eingriff_privatleben_notwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Eingriff in einer demokratischen Gesellschaft notwendig ist"
    reference = "SR 0.101 Art. 8 Abs. 2"


class emrk_eingriff_privatleben_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Eingriff in das Privatleben nach Art. 8 Abs. 2 EMRK zulaessig ist"
    reference = "SR 0.101 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        gesetzlich = person('emrk_eingriff_privatleben_gesetzlich', period)
        notwendig = person('emrk_eingriff_privatleben_notwendig', period)
        return gesetzlich * notwendig
