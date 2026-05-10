"""SR 981 Art. 3

Generated from: ch/de/981.md

Commission: the Federal Council appoints a "Commission for Foreign
Compensations" composed of federal administration representatives
and other experts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kommission_auslaendische_entschaedigungen_bestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat die Kommission fuer auslaendische Entschaedigungen bestellt hat"
    reference = "SR 981 Art. 3"


class kommission_zusammensetzung_bundesverwaltung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission aus Vertretern der Bundesverwaltung und Sachverstaendigen zusammengesetzt ist"
    reference = "SR 981 Art. 3"

    def formula(person, period, parameters):
        return person('kommission_auslaendische_entschaedigungen_bestellt', period)
