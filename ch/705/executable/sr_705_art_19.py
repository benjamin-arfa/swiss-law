"""SR 705 Art. 19 - Fristen fuer die Erstellung und Umsetzung der Plaene

Generated from: ch/de/705.md
Plans must be created within 5 years and implemented within 20 years
of entry into force (1 Jan 2023). Extensions possible by UVEK.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class velowegnetzplan_erstellungsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Erstellung der Velowegnetzplaene in Jahren ab Inkrafttreten"
    reference = "SR 705 Art. 19 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return 5


class velowegnetzplan_umsetzungsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Umsetzung der Velowegnetzplaene in Jahren ab Inkrafttreten"
    reference = "SR 705 Art. 19 Abs. 1 lit. b"

    def formula(person, period, parameters):
        return 20
