"""SR 311.6 Art. 3

Generated from: ch/311/de/311.6.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class busse_gesichtsverhuelllung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Busse bei Verstoss gegen das Verhuellungsverbot (max. 1000 CHF)"
    reference = "SR 311.6 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        verboten = person('gesichtsverhuelllung_verboten', period)
        # Maximum fine is 1000 CHF; actual amount determined by authority
        return verboten * 1000.0


class busse_gesichtsverhuelllung_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag der Busse bei Verstoss gegen das Verhuellungsverbot"
    reference = "SR 311.6 Art. 3 Abs. 1"
    default_value = 1000.0
