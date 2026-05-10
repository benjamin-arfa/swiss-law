"""SR 351.11 Art. 13

Generated from: ch/351/de/351.11.md
Cost distribution between federal and cantonal authorities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bundesbehoerde_ordnet_haft_an(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Bundesbehoerde hat die Haft angeordnet"
    reference = "SR 351.11 Art. 13 Abs. 2"


class bund_traegt_haftkosten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bund traegt die Kosten fuer Haft und damit verbundene Massnahmen"
    reference = "SR 351.11 Art. 13 Abs. 2"

    def formula(person, period):
        return person('bundesbehoerde_ordnet_haft_an', period)


class kosten_art_79a_bst_b(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten aus Anwendung von Art. 79a Bst. b IRSG in CHF"
    reference = "SR 351.11 Art. 13 Abs. 1bis"


class kanton_belastet_fuer_79a(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dem Kanton belastete Kosten fuer Art. 79a Bst. b in CHF"
    reference = "SR 351.11 Art. 13 Abs. 1bis"

    def formula(person, period):
        return person('kosten_art_79a_bst_b', period)
