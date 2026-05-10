"""SR 321.1 Art. 3

Generated from: ch/321/de/321.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rehabilitierung_von_gesetzes_wegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Rehabilitierung erfolgt von Gesetzes wegen (automatisch, ohne Antrag)"
    reference = "SR 321.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return person('faellt_unter_rehabilitierungsgesetz', period)


class aufhebung_urteile_und_entscheide(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Urteile und Entscheide betreffend Strafen, Massnahmen oder Nebenstrafen sind aufgehoben"
    reference = "SR 321.1 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        return person('rehabilitierung_von_gesetzes_wegen', period)
