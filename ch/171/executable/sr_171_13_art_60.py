"""SR 171.13 Art. 60

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindestanzahl_namensaufruf(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestanzahl Ratsmitglieder, die einem Ordnungsantrag auf Namensaufruf zustimmen müssen"
    reference = "SR 171.13 Art. 60 Abs. 1"

    def formula(person, period, parameters):
        return 30
