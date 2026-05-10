"""SR 142.201.1 Art. 6

Generated from: ch/142/de/142.201.1.md

Familiennachzug von Staatsangehoerigen von Nichtmitgliedstaaten der EU
oder der EFTA: Bewilligungen, die dem SEM zur Zustimmung zu unterbreiten sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class familiennachzug_nach_ablauf_frist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Familiennachzug nach Ablauf der Frist nach Art. 47 AIG und Art. 73 VZAE"
    reference = "SR 142.201.1 Art. 6 Bst. a"


class nachkommen_schweizer_ueber_18(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Nachkomme von Schweizer/in ueber 18 Jahre (Art. 42 Abs. 2 AIG)"
    reference = "SR 142.201.1 Art. 6 Bst. b"


class familienangehoerige_aufsteigende_linie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Familienangehoerige/r in aufsteigender Linie (Art. 42 Abs. 2 AIG)"
    reference = "SR 142.201.1 Art. 6 Bst. c"


class zustimmung_sem_familiennachzug_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Zustimmung des SEM fuer Familiennachzug erforderlich"
    reference = "SR 142.201.1 Art. 6"

    def formula(person, period, parameters):
        nicht_eu = person('ist_staatsangehoeriger_nicht_eu_efta', period)
        return nicht_eu * (
            person('familiennachzug_nach_ablauf_frist', period)
            + person('nachkommen_schweizer_ueber_18', period)
            + person('familienangehoerige_aufsteigende_linie', period)
        ) > 0
