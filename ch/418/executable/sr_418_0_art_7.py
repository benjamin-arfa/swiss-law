"""SR 418.0 Art. 7

Generated from: ch/418/de/418.0.md

Bezeichnung von Schweizerschulen im Ausland und ihr Erscheinungsbild.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_anerkannte_schweizerschule(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine nach diesem Gesetz anerkannte Schweizerschule"
    reference = "SR 418.0 Art. 7 Abs. 1"


class darf_bezeichnung_schweizerschule_verwenden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darf die Bezeichnung Schweizerschule verwenden"
    reference = "SR 418.0 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_anerkannte_schweizerschule', period)
