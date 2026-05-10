"""SR 0.101 Art. 11

Generated from: ch/0/de/0.101.md

Freedom of assembly and association: Everyone has the right to freedom
of peaceful assembly and to freedom of association, including the right
to form and join trade unions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_versammlungsfreiheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Versammlungs- und Vereinigungsfreiheit gilt"
    reference = "SR 0.101 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_recht_gewerkschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Gruendung und Beitritt zu Gewerkschaften gilt"
    reference = "SR 0.101 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_versammlungsfreiheit_einschraenkung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Versammlungsfreiheit nach Art. 11 Abs. 2 zulaessig ist"
    reference = "SR 0.101 Art. 11 Abs. 2"
