"""SR 173.110.3 Art. 1

Generated from: ch/173/de/173.110.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class samstag_ist_feiertag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Samstag wird einem anerkannten Feiertag gleichgestellt (Fristenlauf)"
    reference = "SR 173.110.3 Art. 1"

    def formula(person, period, parameters):
        # Art. 1: Samstag wird fuer gesetzliche Fristen des eidgenoessischen Rechts
        # einem anerkannten Feiertag gleichgestellt
        return person('alter', period) * 0 + 1
