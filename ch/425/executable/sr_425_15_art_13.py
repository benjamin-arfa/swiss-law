"""SR 425.15 Art. 13

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_praesident_in_institutsrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Praesidentin oder Praesident des Institutsrats"
    reference = "SR 425.15 Art. 13 Abs. 1"


class sitzungstaggeld(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Sitzungstaggeld pro Sitzungstag in CHF (inkl. Vor- und Nachbereitung)"
    reference = "SR 425.15 Art. 13 Abs. 1-2"

    def formula(person, period, parameters):
        ist_praesident = person('ist_praesident_in_institutsrat', period)
        return where(ist_praesident, 2500.0, 2000.0)
