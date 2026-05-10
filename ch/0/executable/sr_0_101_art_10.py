"""SR 0.101 Art. 10

Generated from: ch/0/de/0.101.md

Freedom of expression: Everyone has the right to freedom of expression,
including freedom to hold opinions and to receive and impart information.
Subject to lawful restrictions necessary in a democratic society.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_meinungsfreiheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf freie Meinungsaeusserung gilt"
    reference = "SR 0.101 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_meinungsfreiheit_einschraenkung_gesetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Meinungsfreiheit gesetzlich vorgesehen ist"
    reference = "SR 0.101 Art. 10 Abs. 2"


class emrk_meinungsfreiheit_einschraenkung_notwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Meinungsfreiheit in einer demokratischen Gesellschaft notwendig ist"
    reference = "SR 0.101 Art. 10 Abs. 2"


class emrk_meinungsfreiheit_einschraenkung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Meinungsfreiheit nach Art. 10 Abs. 2 EMRK zulaessig ist"
    reference = "SR 0.101 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        gesetzlich = person('emrk_meinungsfreiheit_einschraenkung_gesetzlich', period)
        notwendig = person('emrk_meinungsfreiheit_einschraenkung_notwendig', period)
        return gesetzlich * notwendig
