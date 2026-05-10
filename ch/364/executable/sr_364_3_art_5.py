"""SR 364.3 Art. 5

Generated from: ch/364/de/364.3.md

Transporte auf dem Luftweg: Zulaessige Zwangsmittel.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transport_auf_luftweg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person wird auf dem Luftweg transportiert und untersteht Freiheitsbeschraenkungen"
    reference = "SR 364.3 Art. 5"


class zwangsmittel_lufttransport_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zwangsmittel ist bei Transporten auf dem Luftweg zulaessig"
    reference = "SR 364.3 Art. 5"

    def formula(person, period, parameters):
        luftweg = person('transport_auf_luftweg', period)
        typ = person('zwangsmittel_typ', period)
        # Nur nicht-metallische Fesselungsmittel und Schlag-/Abwehrstoecke
        zulaessig = (typ == 'fesselung') + (typ == 'schlagstock')
        return luftweg * zulaessig
