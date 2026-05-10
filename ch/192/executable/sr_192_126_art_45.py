"""SR 192.126 Art. 45

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lohn_steuerbefreit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Lohn ist von der Besteuerung in der Schweiz befreit (Art. 45)"
    reference = "SR 192.126 Art. 45"

    def formula(person, period, parameters):
        # Art. 45: Lohn ist von Besteuerung befreit, sofern Arbeitgeber Vorrechte geniesst
        return person('erfuellt_allgemeine_voraussetzungen', period)
