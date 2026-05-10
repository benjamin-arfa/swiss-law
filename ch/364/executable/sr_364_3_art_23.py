"""SR 364.3 Art. 23

Generated from: ch/364/de/364.3.md

Fesselung waehrend des Transportes: Zulaessige Gruende und Bedingungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fluchtgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fluchtgefahr besteht"
    reference = "SR 364.3 Art. 23 Abs. 1 Bst. a"


class angriffsgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gefahr von Angriffen besteht"
    reference = "SR 364.3 Art. 23 Abs. 1 Bst. b"


class selbstverletzungsgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gefahr von Selbstverletzungen besteht"
    reference = "SR 364.3 Art. 23 Abs. 1 Bst. c"


class fesselung_waehrend_transport_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fesselung waehrend des Transports ist zulaessig"
    reference = "SR 364.3 Art. 23 Abs. 1"

    def formula(person, period, parameters):
        flucht = person('fluchtgefahr', period)
        angriff = person('angriffsgefahr', period)
        selbst = person('selbstverletzungsgefahr', period)
        return flucht + angriff + selbst
