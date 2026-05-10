"""SR 371 Art. 3 - Aufhebung der Strafurteile (Annulment of Convictions)

Generated from: ch/de/371.md
All final convictions by military justice and civilian criminal courts
against refugee helpers per Art. 1 and 2 are annulled.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class strafurteil_aufgehoben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafurteil gegen Fluechtlingshelfer ist von Gesetzes wegen aufgehoben"
    reference = "SR 371 Art. 3"

    def formula(person, period, parameters):
        return person('gilt_als_fluechtlingshelfer', period)
