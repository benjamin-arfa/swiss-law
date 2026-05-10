"""SR 321.0 Art. 44

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class untersuchungshaft_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ausgestandene Untersuchungshaft in Tagen"
    reference = "SR 321.0 Art. 44"


class anrechnung_untersuchungshaft_tagessaetze(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anrechnung der Untersuchungshaft auf die Strafe (1 Tag Haft = 1 Tagessatz Geldstrafe)"
    reference = "SR 321.0 Art. 44"

    def formula(person, period, parameters):
        return person('untersuchungshaft_tage', period)
