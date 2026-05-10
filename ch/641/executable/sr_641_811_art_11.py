"""SR 641.811 Art. 11 - Transport von Rohholz (Timber transport)

1. Vehicles transporting exclusively timber: 75% of standard rates
2. Mixed-use vehicles: refund of CHF 2.10 per m3 of timber transported,
   max 25% of total tax per vehicle and period.

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class svav_rohholz_ausschliesslich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Fahrzeug transportiert ausschliesslich Rohholz (Art. 11 Abs. 1 SVAV)"
    reference = "SR 641.811 Art. 11 Abs. 1"


class svav_rohholz_kubikmeter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Transportierte Kubikmeter Rohholz (Art. 11 Abs. 2 SVAV)"
    reference = "SR 641.811 Art. 11 Abs. 2"


class svav_rohholz_ermaessigung_faktor(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Ermaessigungsfaktor fuer Rohholztransporte (Art. 11 Abs. 1 SVAV)"
    reference = "SR 641.811 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        ausschliesslich = person('svav_rohholz_ausschliesslich', period)
        # Exclusive timber transport pays 75% of standard rate
        return ausschliesslich * 0.75 + (1 - ausschliesslich) * 1.0


class svav_rohholz_rueckerstattung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Rueckerstattung fuer Rohholztransport in CHF (Art. 11 Abs. 2 SVAV)"
    reference = "SR 641.811 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        ausschliesslich = person('svav_rohholz_ausschliesslich', period)
        m3 = person('svav_rohholz_kubikmeter', period)
        # CHF 2.10 per m3 for non-exclusive timber transport
        return (1 - ausschliesslich) * m3 * 2.10
