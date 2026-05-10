"""SR 0.101 Art. 9

Generated from: ch/0/de/0.101.md

Freedom of thought, conscience and religion: Everyone has the right to
freedom of thought, conscience and religion, including freedom to change
religion and to manifest religion. Subject to lawful limitations necessary
in a democratic society.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_gedankenfreiheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Gedanken-, Gewissens- und Religionsfreiheit gilt"
    reference = "SR 0.101 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_religionsfreiheit_einschraenkung_gesetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Religionsfreiheit gesetzlich vorgesehen ist"
    reference = "SR 0.101 Art. 9 Abs. 2"


class emrk_religionsfreiheit_einschraenkung_notwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Religionsfreiheit in einer demokratischen Gesellschaft notwendig ist"
    reference = "SR 0.101 Art. 9 Abs. 2"


class emrk_religionsfreiheit_einschraenkung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Religionsfreiheit nach Art. 9 Abs. 2 EMRK zulaessig ist"
    reference = "SR 0.101 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        gesetzlich = person('emrk_religionsfreiheit_einschraenkung_gesetzlich', period)
        notwendig = person('emrk_religionsfreiheit_einschraenkung_notwendig', period)
        return gesetzlich * notwendig
