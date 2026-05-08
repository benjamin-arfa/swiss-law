"""SR 124 Art. 3 - Konsultation (Consultation)

Generated from: ch/de/124.md
For domestic tasks: consult department security officer.
For foreign tasks: consult EDA and VBS.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class sicherheitseinsatz_inland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schutzaufgabe wird in der Schweiz wahrgenommen"
    reference = "SR 124 Art. 3 Abs. 1"
    default_value = False


class sicherheitseinsatz_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schutzaufgabe wird im Ausland wahrgenommen"
    reference = "SR 124 Art. 3 Abs. 2"
    default_value = False
