"""SR 313.32 Art. 17

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gebuehrenfreiheit_behoerden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Behoerden des Bundes, der Kantone und Gemeinden sind von Kanzleigebuehren befreit"
    reference = "SR 313.32 Art. 17"


class ist_behoerde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handelt es sich um eine Behoerde des Bundes, eines Kantons oder einer Gemeinde"
    reference = "SR 313.32 Art. 17"


class kanzleigebuehr_geschuldet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Kanzleigebuehr geschuldet (nicht von Behoerden)"
    reference = "SR 313.32 Art. 17"

    def formula(person, period, parameters):
        behoerde = person('ist_behoerde', period)
        return not_(behoerde)
