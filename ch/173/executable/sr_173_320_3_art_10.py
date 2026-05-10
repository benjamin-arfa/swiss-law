"""SR 173.320.3 Art. 10

Generated from: ch/173/de/173.320.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zahlungsfrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Zahlungsfrist ab Faelligkeit in Tagen (Art. 10 Abs. 2)"
    reference = "SR 173.320.3 Art. 10"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 20

class verjaehrungsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Verjaehrungsfrist der Gebuehrenforderung in Jahren (Art. 10 Abs. 3)"
    reference = "SR 173.320.3 Art. 10"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 5
