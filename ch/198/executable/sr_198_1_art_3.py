"""SR 198.1 Art. 3

Generated from: ch/198/de/198.1.md

Einsatzplaene und Gegenmassnahmen: Parties conducting activities in the
Antarctic must take countermeasures in environmental emergencies at their
own expense. For state activities, EDA prepares contingency plans. For
non-state activities, the operating party prepares the plans.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fuehrt_taetigkeit_in_antarktis_durch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person fuehrt eine Taetigkeit in der Antarktis durch"
    reference = "SR 198.1 Art. 3 Abs. 1"


class umweltgefaehrdender_notfall_antarktis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt ein umweltgefaehrdender Notfall in der Antarktis vor"
    reference = "SR 198.1 Art. 3 Abs. 1"


class ist_staatliche_taetigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um eine staatliche Taetigkeit"
    reference = "SR 198.1 Art. 3 Abs. 2"


class gegenmassnahmen_pflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pflicht zur Ergreifung von Gegenmassnahmen nach Art. 15 Abs. 1 Bst. a des Protokolls"
    reference = "SR 198.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        taetigkeit = person('fuehrt_taetigkeit_in_antarktis_durch', period)
        notfall = person('umweltgefaehrdender_notfall_antarktis', period)
        return taetigkeit * notfall


class einsatzplan_durch_eda(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einsatzplaene werden durch das EDA aufgestellt (staatliche Taetigkeit)"
    reference = "SR 198.1 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        taetigkeit = person('fuehrt_taetigkeit_in_antarktis_durch', period)
        staatlich = person('ist_staatliche_taetigkeit', period)
        return taetigkeit * staatlich


class einsatzplan_durch_partei(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einsatzplaene werden durch die durchfuehrende Partei aufgestellt (nichtstaatliche Taetigkeit)"
    reference = "SR 198.1 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        taetigkeit = person('fuehrt_taetigkeit_in_antarktis_durch', period)
        staatlich = person('ist_staatliche_taetigkeit', period)
        return taetigkeit * (1 - staatlich)
