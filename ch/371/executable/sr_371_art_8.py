"""SR 371 Art. 8 - Frist (Deadline)

Generated from: ch/de/371.md
Applications must be filed within 5 years of entry into force.
Late applications (up to 8 years) may be accepted if reasons are excusable.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class rehabilitierung_gesuchsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ordentliche Frist fuer Rehabilitierungsgesuche in Jahren ab Inkrafttreten"
    reference = "SR 371 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return 5


class rehabilitierung_nachfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ausserordentliche Nachfrist bei entschuldbarer Verspaetung in Jahren ab Inkrafttreten"
    reference = "SR 371 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        return 8
