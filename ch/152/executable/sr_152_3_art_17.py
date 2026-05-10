"""SR 152.3 Art. 17

Generated from: ch/152/de/152.3.md

Kostenloser Zugang zu amtlichen Dokumenten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_erfordert_aufwendige_bearbeitung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Zugangsgesuch eine besonders aufwendige Bearbeitung erfordert"
    reference = "SR 152.3 Art. 17 Abs. 2"


class ist_schlichtungs_oder_verfuegungsverfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein Schlichtungs- oder Verfuegungsverfahren handelt"
    reference = "SR 152.3 Art. 17 Abs. 3"


class gebuehrenpflichtig_bgoe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Gebuehren erhoben werden koennen"
    reference = "SR 152.3 Art. 17"

    def formula(person, period, parameters):
        aufwendig = person('gesuch_erfordert_aufwendige_bearbeitung', period)
        schlichtung = person('ist_schlichtungs_oder_verfuegungsverfahren', period)
        # Grundsatz: keine Gebuehren. Ausnahme: besonders aufwendig, aber nie in Schlichtung/Verfuegung
        return aufwendig * (1 - schlichtung)
