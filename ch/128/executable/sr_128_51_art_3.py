"""SR 128.51 Art. 3

Generated from: ch/128/de/128.51.md

Halterabfragen: BACS may query domain name holder contact details from the
registry operator in case of imminent cyber threats or ongoing cyberattacks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unmittelbare_cyberbedrohung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine unmittelbare Cyberbedrohung vorliegt"
    reference = "SR 128.51 Art. 3"


class laufender_cyberangriff(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein laufender Cyberangriff vorliegt"
    reference = "SR 128.51 Art. 3"


class bacs_darf_halterabfrage_durchfuehren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BACS Kontaktangaben der Domain-Halter abfragen darf"
    reference = "SR 128.51 Art. 3"

    def formula(person, period, parameters):
        bedrohung = person('unmittelbare_cyberbedrohung', period)
        angriff = person('laufender_cyberangriff', period)
        return bedrohung + angriff > 0
