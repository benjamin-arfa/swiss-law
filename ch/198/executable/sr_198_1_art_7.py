"""SR 198.1 Art. 7

Generated from: ch/198/de/198.1.md

Strafrechtspflege: Criminal offences under this law are prosecuted and
judged by the authorities of the Canton of Basel-Stadt. Fines imposed
under this law go to the Canton of Basel-Stadt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strafrechtspflege_kanton_basel_stadt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafbare Handlungen nach diesem Gesetz werden von Basel-Stadt verfolgt und beurteilt"
    reference = "SR 198.1 Art. 7"

    def formula(person, period, parameters):
        return True


class geldstrafen_verfuegung_kanton_basel_stadt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueber die Geldstrafen verfuegt der Kanton Basel-Stadt"
    reference = "SR 198.1 Art. 7"

    def formula(person, period, parameters):
        return True
