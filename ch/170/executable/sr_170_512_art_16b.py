"""SR 170.512 Art. 16b

Generated from: ch/170/de/170.512.md

Datenschutz bei Veröffentlichungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class veroeffentlichung_enthaelt_besonders_schuetzenswerte_daten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veröffentlichung enthält besonders schützenswerte Personendaten (Art. 16b Abs. 1 PublG)"
    reference = "SR 170.512, Art. 16b Abs. 1"


class online_zugaenglichkeit_beschraenkt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Online-Zugänglichkeit muss zeitlich und inhaltlich beschränkt werden (Art. 16b Abs. 2 PublG)"
    reference = "SR 170.512, Art. 16b Abs. 2"

    def formula(person, period, parameters):
        return person('veroeffentlichung_enthaelt_besonders_schuetzenswerte_daten', period)
