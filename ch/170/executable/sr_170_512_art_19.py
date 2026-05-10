"""SR 170.512 Art. 19

Generated from: ch/170/de/170.512.md

Gebühren: Konsultation der Plattform ist unentgeltlich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class konsultiert_publikationsplattform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konsultiert die Publikationsplattform (Art. 19 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 19 Abs. 1"


class gebuehr_konsultation(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebühr für Konsultation der Publikationsplattform in CHF (Art. 19 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 19 Abs. 1"

    def formula(person, period, parameters):
        # Die Konsultation ist unentgeltlich
        return person('konsultiert_publikationsplattform', period) * 0
