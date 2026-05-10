"""SR 427.72 Art. 11

Generated from: ch/427/de/427.72.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindest_archivierungsdauer_primaerdaten_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindest-Archivierungsdauer fuer Primaerdaten und Forschungsprotokolle nach Abschluss in Jahren"
    reference = "SR 427.72 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        return 5
