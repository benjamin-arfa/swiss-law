"""SR 0.101 Art. 4

Generated from: ch/0/de/0.101.md

Prohibition of slavery and forced labour: No one shall be held in
slavery or servitude. No one shall be required to perform forced or
compulsory labour, with specified exceptions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_verbot_sklaverei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verbot der Sklaverei und Leibeigenschaft gilt"
    reference = "SR 0.101 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_verbot_zwangsarbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verbot der Zwangs- oder Pflichtarbeit gilt"
    reference = "SR 0.101 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_arbeit_bei_freiheitsentzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine uebliche Arbeit bei Freiheitsentzug nach Art. 5 vorliegt (keine Zwangsarbeit)"
    reference = "SR 0.101 Art. 4 Abs. 3 Bst. a"


class emrk_militaerdienst_oder_ersatzdienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob militaerischer Dienst oder Ersatzdienst vorliegt (keine Zwangsarbeit)"
    reference = "SR 0.101 Art. 4 Abs. 3 Bst. b"


class emrk_dienstleistung_notstand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Dienstleistung bei Notstand oder Katastrophe vorliegt (keine Zwangsarbeit)"
    reference = "SR 0.101 Art. 4 Abs. 3 Bst. c"


class emrk_uebliche_buergerpflichten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob uebliche Buergerpflichten vorliegen (keine Zwangsarbeit)"
    reference = "SR 0.101 Art. 4 Abs. 3 Bst. d"
