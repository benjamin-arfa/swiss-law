"""SR 173.320.3 Art. 6

Generated from: ch/173/de/173.320.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class faxkosten_inland_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Faxkosten pro Seite Inland in CHF (Art. 6 lit. c)"
    reference = "SR 173.320.3 Art. 6"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 1.0

class faxkosten_ausland_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Faxkosten pro Seite Ausland in CHF (Art. 6 lit. c)"
    reference = "SR 173.320.3 Art. 6"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 2.0

class mahnkosten_erste_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mahnkosten erste Mahnung in CHF (Art. 6 lit. e)"
    reference = "SR 173.320.3 Art. 6"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 10.0

class mahnkosten_weitere_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mahnkosten ab zweiter Mahnung in CHF (Art. 6 lit. e)"
    reference = "SR 173.320.3 Art. 6"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 20.0
