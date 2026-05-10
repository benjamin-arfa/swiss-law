"""SR 442.132.3 Art. 5a

Generated from: ch/442/de/442.132.3.md

Ueberschreiten des Hoechstbetrags der Lohnklasse: Max 5% ueber Hoechstbetrag
zur Personalgewinnung/-erhaltung. Max 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hoechstbetrag_lohnklasse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstbetrag der Lohnklasse (CHF)"
    reference = "SR 442.132.3 Art. 5a Abs. 1"


class max_lohn_mit_ueberschreitung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Lohn inkl. 5% Ueberschreitung zur Personalgewinnung"
    reference = "SR 442.132.3 Art. 5a Abs. 1"

    def formula(person, period, parameters):
        hoechst = person('hoechstbetrag_lohnklasse', period)
        return hoechst * 1.05
