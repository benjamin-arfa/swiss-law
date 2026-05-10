"""SR 746.1 Art. 2

Generated from: ch/746/de/746.1.md

Plangenehmigung fuer Rohrleitungsanlagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class benoetigt_plangenehmigung_rohrleitung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rohrleitungsanlage benoetigt eine Plangenehmigung der Aufsichtsbehoerde"
    reference = "SR 746.1 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        # Art. 2 Abs. 1: Rohrleitungsanlagen nach Art. 1 Abs. 2 duerfen
        # nur mit einer Plangenehmigung erstellt oder geaendert werden.
        return person('unterliegt_rohrleitungsgesetz_voll', period)


class plangenehmigung_umfasst_alle_bundesbewilligungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mit der Plangenehmigung werden saemtliche nach Bundesrecht erforderlichen Bewilligungen erteilt"
    reference = "SR 746.1 Art. 2 Abs. 3"
    default_value = True


class kantonale_bewilligungen_rohrleitung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kantonale Bewilligungen und Plaene sind nicht erforderlich (Art. 2 Abs. 4)"
    reference = "SR 746.1 Art. 2 Abs. 4"
    default_value = False
