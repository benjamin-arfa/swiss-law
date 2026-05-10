"""SR 453.0 Art. 25

Generated from: ch/453/de/453.0.md
Anerkennungsverfahren - Dauer 2 Jahre, Erneuerung von Amtes wegen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anerkennung_datum_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der letzten Anerkennung als wissenschaftliche Einrichtung"
    reference = "SR 453.0 Art. 25 Abs. 1"


class anerkennung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anerkennung ist noch gueltig (2 Jahre, wird von Amtes wegen erneuert)"
    reference = "SR 453.0 Art. 25 Abs. 1"

    def formula(person, period, parameters):
        datum = person('anerkennung_datum_jahr', period)
        aktuelles_jahr = period.start.year
        return (aktuelles_jahr - datum) <= 2
